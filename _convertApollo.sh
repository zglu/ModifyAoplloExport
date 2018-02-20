#!/bin/bash

# apollo gff to Augustus gff 
## first remove # and empty lines 
cat input.gff | grep -v '#' | grep -v -e '^$' > input-ed.gff

# python script to transform the style
python modifyGFF.py input-ed.gff > input_out.gff

# get single gff with mRNA and CDS
cat input_out.gff | grep 'mRNA\|CDS' > input_utr.gff
cat input_utr.gff | grep mRNA | awk '{print $9}'|cut -d \; -f1 | sed 's/ID=//' > ids
for id in `cat ids`; do cat input_utr.gff |grep $id > ./$id.utr.gff; done

# calculate UTR
for i in *.utr.gff; do python calcUTR.py $i > $i.utr.gff3; done

# combine modified gff and utr
cat input_out.gff *.utr.gff3 > output.gff

rm -rf *.utr.gff* input_utr.gff ids input-ed.gff input_out.gff  

# check if utr lenght end up with -1
echo 'UTRs with length < 1:'
cat output.gff | grep UTR | awk '{print $3 " " $5-$4 " " $9}'| awk '$2<0'

## check duplicate annotations
echo 'DUPLICATE IDs:'
cat output.gff | grep gene | awk '{print $9}'| sort | uniq -c | sort -rnk1 | awk '$1>1'


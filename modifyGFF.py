#! /usr/bin/env python

'''
modify GFF from Apollo to Augustus style
this will take transcript name as it is; can have multiple gene features
must be in gene -> mRNA -> cds/exon order
first remove comment and empty lines: grep -v '#' | grep -v -e '^$'
'''

# last update: 08/02/2018

import re
import sys

GFF = sys.argv[1] # gff with many genes


with open(GFF) as fin:
    for line in fin:
        line = line.rstrip()
        line = line.split()
        try:
            if any(s in line for s in ("gene", "pseudogene")):
                name_pat = re.compile("Name=(.+?);")
                geneid = name_pat.search(line[8]).group(1)
                line[8] = "ID=" + geneid
            elif any(s in line for s in ("mRNA", "transcript")):
                mrnaid_pat = re.compile("ID=(.+?);")
                mrnaid = mrnaid_pat.search(line[8]).group(1)
                trid_pat = re.compile("Name=(.+?);")
                trid = trid_pat.search(line[8]).group(1)
                line[8] = "ID=" + trid + ";" + "Parent=" + geneid
            elif any(s in line for s in ("exon", "non_canonical_three_prime_splice_site", "non_canonical_five_prime_splice_site")):
                line[8] = line[8].replace(mrnaid, trid)
                line[8] = re.sub(";ID=(.+)", "", line[8])
                line[8] = re.sub("Name=(.+)", "", line[8])
            elif "CDS" in line:
                line[8] = line[8].replace(mrnaid, trid)
                line[8] = re.sub("Parent=(.+?);", "", line[8])
                line[8] = re.sub("ID=(.+);", "ID=" + trid + ".cds;Parent=" + trid, line[8])
                line[8] = re.sub("Name=(.+)", "", line[8])
            line[1] = "Apollo"
            print("\t".join(line))
        except (AttributeError, NameError):
            pass

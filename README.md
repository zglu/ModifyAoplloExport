# ModifyAoplloExport

Modify the gff export from Apollo, changing Name to ID to reserve more meaningful words. 

For instance, the following export will be modified to:

~~~~~~
SM_V7_ZW        iris    gene    52309880        52312410        .       -       .       owner=alt@sanger.ac.uk;ID=38776c44-0fa6-4d5e-a3c0-4d5d3a359faf;date_last_modified=2018-01-23;Name=Smp_336850;date_creation=2018-01-23
SM_V7_ZW        iris    mRNA    52309880        52312410        .       -       .       owner=alt@sanger.ac.uk;Parent=38776c44-0fa6-4d5e-a3c0-4d5d3a359faf;ID=ea036c7f-a83e-4873-aef5-bccca601ef9c;date_last_modified=2018-01-23;Name=Smp_336850.1;date_creation=2018-01-23
SM_V7_ZW        iris    CDS     52311450        52311467        .       -       0       Parent=ea036c7f-a83e-4873-aef5-bccca601ef9c;ID=ea036c7f-a83e-4873-aef5-bccca601ef9c-CDS;Name=ea036c7f-a83e-4873-aef5-bccca601ef9c-CDS
SM_V7_ZW        iris    CDS     52309880        52310784        .       -       0       Parent=ea036c7f-a83e-4873-aef5-bccca601ef9c;ID=ea036c7f-a83e-4873-aef5-bccca601ef9c-CDS;Name=ea036c7f-a83e-4873-aef5-bccca601ef9c-CDS
SM_V7_ZW        iris    exon    52311450        52312410        .       -       .       Parent=ea036c7f-a83e-4873-aef5-bccca601ef9c;ID=d4c7fca8-6407-402c-a230-647a10aa24b4;Name=d4c7fca8-6407-402c-a230-647a10aa24b4
SM_V7_ZW        iris    exon    52309880        52310784        .       -       .       Parent=ea036c7f-a83e-4873-aef5-bccca601ef9c;ID=61148130-f429-443e-bbda-6a8dc1d3549a;Name=61148130-f429-443e-bbda-6a8dc1d3549a
~~~~~~

Which looks more tranditional output from gene predictor (e.g., Augustus):

~~~~~~
SM_V7_ZW	Apollo	gene	52309880	52312410	.	-	.	ID=Smp_336850
SM_V7_ZW	Apollo	mRNA	52309880	52312410	.	-	.	ID=Smp_336850.1;Parent=Smp_336850
SM_V7_ZW	Apollo	CDS	52311450	52311467	.	-	0	ID=Smp_336850.1.cds;Parent=Smp_336850.1
SM_V7_ZW	Apollo	CDS	52309880	52310784	.	-	0	ID=Smp_336850.1.cds;Parent=Smp_336850.1
SM_V7_ZW	Apollo	exon	52311450	52312410	.	-	.	Parent=Smp_336850.1
SM_V7_ZW	Apollo	exon	52309880	52310784	.	-	.	Parent=Smp_336850.1
~~~~~~

## Usage

~~~~~~
./pipeline.sh
~~~~~~

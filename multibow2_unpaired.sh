#!/bin/sh
#Run bowtie2 against multiple fastq files as unpaired reads
#Options for bowtie2 are set to --no-unal, --no-hd, --no-sq, --fast-local and -q

for i in "$@"
do
    bowtie2 --no-unal --no-hd --no-sq --local -D 10 -R 2 -N 0 -L 22 -i S,1,1.75 -q -x ~/src/DB/phiX174.fasta.index -U $i -S $i.sam
done

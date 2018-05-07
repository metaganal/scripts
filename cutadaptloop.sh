#!/bin/sh
#Run cutadapt against multiple fastq files
#Options for cutadapt are set to -g GTGCCAGCMGCCGCGGTAA -O 13 -q 17,17 -m 150 -M 290 for 5' primer
#Options for cutadapt are set to -a ATTAGAWACCCVHGTAGTCC -O 13 -q 17,17 -m 150 -M 290 -f fastq for 3' primer

dir=$(dirname $1)

for i in "$@"
do
    base=$(basename $i ".N.rem.pair.merged.fastq")
    cutadapt -g GTGCCAGCMGCCGCGGTAA -O 13 -q 17,17 -m 150 -M 290 -o ${dir}/${base}.trim.cut17.len150290 ${dir}/${base}.N.rem.pair.merged.fastq
    cutadapt -a ATTAGAWACCCVHGTAGTCC -O 13 -q 17,17 -m 150 -M 290 -f fastq -o ${dir}/${base}.trim2.len150290 ${dir}/${base}.trim.cut17.len150290
done

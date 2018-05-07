#!/bin/sh
#Run usearch fastq_mergepairs against multiple pairs of fastq files
#Options for usearch are set to -fastq_trunctail and -fastq_nostagger

dir=$(dirname $1)

for i in "$@"
do
    base=$(basename $i "_1.fastq.N.rem.pair")
    usearch -fastq_mergepairs ${dir}/${base}_1.fastq.N.rem.pair -reverse ${dir}/${base}_2.fastq.N.rem.pair -fastqout ${dir}/${base}.N.rem.pair.merged.fastq -fastq_trunctail -fastq_nostagger
done

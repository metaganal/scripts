#!/bin/sh
#Download from URLs in a tsv

while read NUMBER FTPserver
    do
        wget -nd --directory-prefix="~/FTPdump" -r -np -A.fastq.bz2 "$FTPserver"
    done < "$@"

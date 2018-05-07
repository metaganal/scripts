#!/bin/sh
#Download from all the links provided

for i in "$@"
    do
        curl -O "$i"
    done

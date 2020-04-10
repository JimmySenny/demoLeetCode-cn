#!/bin/bash

ROWS=`wc -l file.txt`
if [ $ROWS gt 10 ]; then
    exit -1;
fi

head -n 10 file.txt | tail -n 1 

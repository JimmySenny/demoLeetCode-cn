#!/bin/bash

awk  '{
    for( i=1;i<=NF;i++){
        if( 1 == NR ){
            row[i] = $i
        }else{
            row[i] = row[i] " " $i
        }
    }
} END {
        for( j=1;j<=NF;j++ ){
            print row[j]
        }
} ' file.txt

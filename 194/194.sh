#!/bin/bash

cat file.txt | awk '{ for(i=1;i<=NF;i++){for(j=1;j<=NR;j++){ print i j } }  }' | 

{ for(i=1;i<=NF;i++){ sum[$i]++}}END {for (j in sum ) print j " " sum[j]}'

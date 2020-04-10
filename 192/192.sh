#!/bin/bash


cat words.txt  | tr ' ' '\n' | sed /^$/d | sort | uniq -c
cat words.txt   | tr '\n' ' ' | awk '{ for(i=1;i<=NF;i++){ sum[$i]++}}END {for (j in sum ) print j " " sum[j]}' 
cat words.txt  | xargs -n 1 | sort | uniq -c


#!/bin/bash

COLUMN_NUM=`awk '{ print NF}' file.txt | uniq`
echo $COLUMN_NUM

#i=1
#while(( i<=$COLUMN_NUM ))
for((i=1;i<=$COLUMN_NUM;i++));
do
    cut -d' ' -f$i file.txt | xargs
done

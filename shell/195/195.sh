#!/bin/bash

awk 'NR==num'  file.txt
tail -n +10 file.txt | head -n 1
sed -n '10p'

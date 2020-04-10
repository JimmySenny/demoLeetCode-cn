#!/bin/bash


cat words.txt  | tr ' ' '\n' | sed /^$/d | sort | uniq -c

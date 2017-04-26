#!/bin/sh
ls -1 *.txt > list.file
while read line; do 
    if [ -f "$line.sig" ]
    then
     echo "$line.sig exists"
    else
     echo "$line.sig does not exist"
    fi   
done < list.file

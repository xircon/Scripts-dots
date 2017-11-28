#!/bin/bash
rm -rf mypac2.txt
pacman -Q > pacman.txt
awk '{print $1}' pacman.txt > mypac.txt
file="mypac.txt"
while IFS=: read -r f1 
do
        f2=`awk '{gsub("Description     :", "");print}' <<< $(yaourt -Qi $f1 | grep Description)`
        echo "$f1" "$f2" >> mypac2.txt
done <"$file"
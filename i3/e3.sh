#!/bin/bash

cd ~/.i3 
rm -f *~
joe ~/.i3/config.conf 
i3bang config.conf 
cp config.conf backup/config.backup.$(date +%F_%R_%S)
i3-msg reload
####### 
#gitup#
####### 
cd ~/scripts
git push --all -u origin 
git add * 
git commit -a -m 'This is a commit' 
git push --all -u origin

cd ~/.i3

#!/bin/bash
#interp=`yad --form --field="ComboBox:CB" python\!python2 |cut -f1 -d\|`
line=`xdotool search  --class featherpad getwindowname %@ | grep -vn featherpad |cut -f1 -d:`
title=`xdotool search  --class featherpad getwindowname %$line`
run="/home/steve/scripts/$title"
eval "$run"
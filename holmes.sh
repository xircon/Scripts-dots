#!/bin/bash
str=`uname -r`
suffix="-MANJARO"
newstr=${str%$suffix}
echo "${newstr}"
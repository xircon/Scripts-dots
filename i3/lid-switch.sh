#!/bin/bash
if [ "$1" = "" ]; then 
   echo "Usage lid-switch.sh on/off"
   exit 
fi

if [ "$1" = "off" ]; then
   systemd-inhibit --what=handle-lid-switch sleep 1d &
 else
   #Basically everything else is on :) 
   killall systemd-inhibit
fi
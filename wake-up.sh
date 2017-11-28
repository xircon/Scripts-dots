#!/usr/bin/env bash
#

# Ensure script is running as root. rtcwake needs sudo access
if [[ $EUID -ne 0 ]]; then
   echo "This script cannot function if it is not run as root" 
   exit 1
fi

today=`date +%A`

if [[ "  Monday Tuesday Wednesday Thursday Friday " =~ " ${today} " ]]; then
	rtcwake -m no -l -t "$(date -d 'tomorrow 07:30:00' '+%s')"
fi
# Account for weekends
if [[ " Saturday Sunday " =~ " ${today} " ]]; then
	rtcwake -m no -l -t "$(date -d 'Monday 07:30:00' '+%s')"
fi

# Example provided for Banshee. This will provide you a GUI to stop the music. Edit for the CLI to the player you use
# If you don't care about a GUI, play would work fine.
banshee --play /path/to/file_or_playlist

#!/bin/bash
######################################################################################################
# This script will toggle minimize/activate first window with specified class
# If window not found program will be launched
#
# window class can be found with next programs:
#   wmctrl -x -l
#   xprop
#
#
# **IMPORTANT**
# No credit taken.......... Cannot read the original.....
# Found on http://blog.sokolov.me/2014/06/20/linuxx11-toggle-window-minimizemaximize/
# in Russian :) but works when adjusting the wrapping.
# Assigned to meta-f in KDE plasma 5
######################################################################################################
NEEDED_WINDOW_CLASS="systemsettings5.systemsettings"
LAUNCH_PROGRAM="kstart --desktop 2 /usr/bin/systemsettings5"
######################################################################################################
NEEDED_WINDOW_WINDOW_ID_HEX=`wmctrl -x -l | grep ${NEEDED_WINDOW_CLASS} | awk '{print $1}' | head -n 1`
NEEDED_WINDOW_WINDOW_ID_DEC=$((${NEEDED_WINDOW_WINDOW_ID_HEX}))
if [ -z "${NEEDED_WINDOW_WINDOW_ID_HEX}" ]; then
    ${LAUNCH_PROGRAM}
else
    echo "Found window ID:${NEEDED_WINDOW_WINDOW_ID_DEC}(0x${NEEDED_WINDOW_WINDOW_ID_HEX})"
    ACIVE_WINDOW_DEC=`xdotool getactivewindow`
    if [ "${ACIVE_WINDOW_DEC}" == "${NEEDED_WINDOW_WINDOW_ID_DEC}" ]; then
        xdotool windowminimize ${NEEDED_WINDOW_WINDOW_ID_DEC}
    else
        xdotool windowactivate ${NEEDED_WINDOW_WINDOW_ID_DEC}
    fi
fi

#!/bin/bash
#
############################################
# Set both shift keys to trigger caps lock #
############################################
setxkbmap -option "caps:none"
setxkbmap -option "shift:both_capslock"

killall xcape

################
# Super Keys:  #
################
xcape -e 'Super_L=Alt_L|Tab'
xcape -e 'Super_R=Super_L|F2'

#################
# Control keys: #
#################
xcape -e 'Control_L=Super_L|1'
xcape -e 'Control_R=Control_R|Return' 

############
# Alt Keys #
############
xcape -e 'Alt_L=Super_L|2'
#Reconfigure Alt_gr
xmodmap -e "keycode 108 = Alt_R" && xset -r 108
xcape -e 'Alt_R=Super_L|a'

##############
# Shift Keys #
##############
xcape -e 'Shift_L=Escape'
xcape -t 200 -e 'Shift_R=Control_L|Alt_L|m'

#############
# Caps Lock #
#############
#Disable caps lock key
xmodmap -e 'clear Lock'
xcape -t 200 -e '#66=Alt_L|m'
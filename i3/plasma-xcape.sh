#!/bin/bash
#

############################################
# Set both shift keys to trigger caps lock #
############################################
setxkbmap -option "shift:both_capslock"

killall xcape

###################
## Super Keys:    #
###################
#xcape -e 'Super_L=Alt_L|Tab'
#xcape -e 'Super_R=Control_L|Alt_L|m'
xmodmap -e "keycode 135 = Super_R"
xmodmap -e "keycode 134 = Super_R"


xcape -e 'Super_R=Control_L|Alt_L|Right'
#xcape -e '#135=Control_L|Alt_L|Right'


###################
## Control Keys:  #
###################
#xcape -e 'Control_L=Control_L|Alt_L|Right'
#xcape -e 'Control_L=F12'
xcape -e 'Control_L=Control_L|Alt_L|t'
xcape -e 'Control_R=Control_L|F10' 

###################
# Alt Keys:       #
###################
xcape -e 'Alt_L=Super_L|w'
#Reconfigure Alt_gr
xmodmap -e "keycode 108 = Alt_R" && xset -r 108
xcape -e 'Alt_R=Super_L|a'
#xcape -e 'Alt_R=EuroSign'


###################
# Shift Keys:     #
###################
xcape -e 'Shift_L=Super_L|d'
xcape -t 200 -e 'Shift_R=Control_L|Shift_L|m'

#############
# Caps Lock #
#############
#Disable caps lock key
xmodmap -e 'clear Lock'
xcape -t 200 -e '#66=Super_L|d'

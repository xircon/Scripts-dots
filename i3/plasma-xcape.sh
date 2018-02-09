#!/bin/bash
#
notify-send Plasma-xcape "xcape starting" 
############################################
# Set both shift keys to trigger caps lock #
############################################
setxkbmap -option caps:none
setxkbmap -option "shift:both_capslock"
setxkbmap -option "terminate:ctrl_alt_bksp"                       

killall xcape

###################
## Super Keys:    #
###################

#xcape -e 'Super_L=Control_L|Alt_L|d'
#xcape -e 'Super_R=Control_L|Alt_L|m'

#Remap MenuKey to Super_R
xmodmap -e "keycode 135 = Super_R"
xmodmap -e "keycode 134 = Super_R"

# Desktop right
xcape -e 'Super_R=Control_L|Alt_L|Right'
#
#xcape -e '#135=Control_L|Alt_L|Right'


###################
## Control Keys:  #
###################
#xcape -e 'Control_L=Control_L|Alt_L|Right'
#xcape -e 'Control_L=F12'

#Control_L - Launch Terminal script:
xcape -e 'Control_L=Control_L|Alt_L|t'

#Control_R - Expo Mode:
xcape -e 'Control_R=Control_L|F10' 

###################
# Alt Keys:       #
###################
#Alt_L- Vivaldi
xcape -e 'Alt_L=Super_L|w'

#Alt_L - Firefox
#xcape -e 'Alt_L=Super_L|f'

#Reconfigure Alt_gr
xmodmap -e "keycode 108 = Alt_R" && xset -r 108
xcape -e 'Alt_R=Super_L|a'

###################
# Shift Keys:     #
###################
#Shift_L - Show Desktop
#xcape -e 'Shift_L=Control_L|Alt_L|d'
xcape -e 'Shift_L=BackSpace|Escape'
#Shift_R - Mute toggle
xcape -t 200 -e 'Shift_R=Control_L|Alt_L|m'

#############
# Caps Lock #
#############
#Disable caps lock key, see above..........
xmodmap -e 'clear Lock'
xcape -t 200 -e '#66=Super_L|d'
notify-send Plasma-xcape "xcape loaded" 
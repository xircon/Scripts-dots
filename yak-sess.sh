#!/bin/bash
yakuake &
sleep 2
yakuake
sleep 2
xdotool key "control+0"
xdotool key "control+9"
xdotool key "control+shift+Up"
xdotool key "control+shift+Up"
yakuake
yakuake-session -t htop -e htop
yakuake-session -t joe -e joe --hold -w /home/steve/scripts
yakuake-session -t scripts -w /home/steve/scripts
yakuake-session -t Twitter -e rainbowstream
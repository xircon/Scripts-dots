#!/usr/bin/env python3

import i3ipc
import os

i3 = i3ipc.Connection()

i3.command('workspace next')

focused = i3.get_tree().find_focused()

wspce=int(focused.workspace().name[:1])

if wspce == 2:
   os.system("killall compton")
else:
   os.system("compton -b")   

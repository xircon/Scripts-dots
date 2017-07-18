import subprocess as sp
import time
print('Now, open a text editor, and focus it IN 10 SECONDS!')
#time.sleep(10); sp.Popen(['xdotool', 'type', 'hello@world'])
#time.sleep(10); sp.Popen(['xdotool', 'type', "'hello@world'"])
time.sleep(10); sp.Popen(['xdotool type hello@world'], shell=True)


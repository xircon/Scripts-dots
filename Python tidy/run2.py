#Source - http://stackoverflow.com/questions/38056/how-do-you-check-in-linux-with-python-if-a-process-is-still-running

import os, time, subprocess

processname = 'firefox'

def cnter():
    tmp = os.popen("ps -Af").read()
    proccount = tmp.count(processname)
    return proccount
    
proc=cnter()    


while proc == 0:
    print(proc)
    time.sleep(5)
    proc=cnter()

print(proc)
subprocess.Popen("medit")

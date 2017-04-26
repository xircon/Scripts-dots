#! /usr/bin/python

import os, time, subprocess

processname = 'mate-panel'

def cnter():
    tmp = os.popen("ps -Af").read()
    proccount = tmp.count(processname)
    return proccount
    
proc=cnter()    


while proc == 0:
    print(proc)
    time.sleep(15)
    proc=cnter()

print(proc)
subprocess.Popen("whatpulse")

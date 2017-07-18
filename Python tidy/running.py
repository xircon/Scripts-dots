#Source - http://stackoverflow.com/questions/38056/how-do-you-check-in-linux-with-python-if-a-process-is-still-running
#!/usr/bin/env python
  
import os, time, datetime, yagmail

processname = 'compton'

def cnter():
    tmp = os.popen("ps -Af").read()
    proccount = tmp.count(processname)
    return proccount
    
proc=cnter()    


while proc > 0:
    print(proc, ' processes running of ', processname, 'type')
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M"))
    time.sleep(60)
    proc=cnter()

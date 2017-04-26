import os

processname = 'cairo-dock'
tmp = os.popen("ps -Af").read()
proccount = tmp.count(processname)

if proccount == 0:
    print(proccount, ' processes running of ', processname, 'type')
    os.system("cairo-dock")

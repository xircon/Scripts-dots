#!/usr/bin/env python
 
from appJar import gui

# the title of the button will be received as a parameter
def press(btn):
   print(btn)

app=gui("Test Layout","500x400")
#app.setPadding(2,2)
# 3 buttons, each calling the same function
app.setSticky("nw")
app.addButton("One  ", press,0,0)
app.addButton("Two  ", press,1,0)
app.addButton("Three", press,2,0)
app.addButton("Four ", press,3,0)
app.addButton("Five ", press,4,0)

app.setSticky("e")
app.addTextArea("t1",1,3)
app.go()

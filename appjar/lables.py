try:
   from xappJar import gui
except:
   print("appjar is not installed!!!")
   print("run - sudo pip install appjar")
   exit()try:
   from xappJar import gui
except:
   print("appjar is not installed!!!")
   print("run - sudo pip install appjar")
   exit()

app = gui()

app.addFlashLabel("f1", "This is flashing")
app.addLabel("f2", "This is not flashing")
app.addFlashLabel("f3", "This is also flashing")

app.go()
from appJar import gui

t1="This is a test"
app=gui()
app.setFg("white")
app.setGeometry("500x300")
app.addTextArea("t1")
app.setTextArea("t1","TESTING TESTING 1 2 3", callFunction=False)
app.setTextAreaBg("t1","lightblue")
app.setTextAreaFg("t1","white")
app.go()
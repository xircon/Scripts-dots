from appJar import gui

app=gui()
app.setGeometry("500x300")
app.setFont(12)
app.setBg("white")
app.addMessage("mess", """This is a test message""")
app.go()
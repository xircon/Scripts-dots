from appJar import gui

app=gui()

app.addEntry("e1")
app.addNumericEntry("e2")
app.addEntry("e3")
app.addLabelEntry("Name")

app.setEntryDefault("e2", "Age here")

app.go()

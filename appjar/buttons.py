from appJar import gui

# the title of the button will be received as a parameter
def press(btn):
    print(btn)

app=gui()
# 3 buttons, each calling the same function
app.addButton("One", press)
app.addButton("Two", press)
app.addButton("Three", press)
app.go()
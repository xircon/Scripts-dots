#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import Appjar Gui
from appJar import gui
from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
import tkinter.font as tkFont


from sh import inxi
a=str(inxi("-Fxzc0"))

#Functions go here.........
def press(btn):
    app.setTextArea("Inxi", a)
    #app.stop()

def guiconfig():
    app.setTitle("Run inxi")
    app.setGeometry("800x500") #Width x Height
    #app.setResizable(canResize=True)
    #app.setTransparency(100) #Not supported in Linux
    app.setBg("lightgreen")
    app.setButtonFont(20, font="Ubuntu Mono")
    app.setLabelFont(20, font="Ubuntu Mono")
    #app.setFont("8", font="Mono")


app = gui()

guiconfig()

app.addTextArea("Inxi")
ta = app.getTextAreaWidget("Inxi")
ta.config(font="Mono 8")
#ta.config(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)
app.addLabel("title", "Run Inxi")  # Row 0,Column 0,Span 2
app.addButton("Press to run inxi", press)

app.go()

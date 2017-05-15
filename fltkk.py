from fltk import *
import sys

def theCancelButtonCallback(ptr):
	sys.exit(0)

window = Fl_Window(100,100,200,90)
window.label(sys.argv[0])
button = Fl_Button(9,20,180,50)
button.label("Hello World")
button.callback(theCancelButtonCallback)
window.end()
window.show(len(sys.argv), sys.argv)
Fl.run()
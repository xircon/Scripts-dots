#!/usr/bin/env python

import subprocess

def run_yad(num, text):
    mytext = '--text=' + ' '.join(map(str, [num, text]))
    timeout = "--timeout=" + dsptime
    subprocess.call([ "yad", "--title", name, '--width=200', '--center', '--button=gtk-ok:0', timeout, mytext])

import tkinter

root = tkinter.Tk()

max_chars = 140
name = "chars"
dsptime='10'

#text_in_clipboard = clipboard.get_selection()
# works outside of autokey with this
text_in_clipboard = root.clipboard_get()
length = len(text_in_clipboard)
count = 140 - length
if count > -1:
    run_yad(count, " Characters left")
else:
    count = -count
    run_yad(count, " Characters over limit")

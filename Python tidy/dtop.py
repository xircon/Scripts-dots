#!/usr/bin/env python
import os
a=os.popen('xprop -root _NET_CURRENT_DESKTOP').read()
os.s
print(a)

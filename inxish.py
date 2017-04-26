f = open('/tmp/mlogsout.txt', 'w') # write mode clears any previous content from the file if it exists

from sh import inxi
f.write(inxi("-Fxzc0"))

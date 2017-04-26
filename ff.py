#!/usr/bin/python
import time
import envoy

r = envoy.run('pgrep -f firefox')

while r.status_code ==  0:
	print("firefox is running")
	r = envoy.run('pgrep -f firefox')
	time.sleep(4)



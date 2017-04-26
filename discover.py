from roku import Roku

import re
import ipaddress

#set your IP here if automatic discovery fails.
#roku = Roku('192.168.0.7')

#Automatic discovery......
a=Roku.discover(timeout=15)
b=str(a[0])
print(a[0], b)

ip = re.compile('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}'
                +'(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')

match = ip.search(b)
#b=ipaddress.ip_address(foo)
c=match.group()
print(c)

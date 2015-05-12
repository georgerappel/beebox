PORT = 50000

import sys
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

#data = str(sys.argv)
#print sys.argv[1]

data_str = sys.argv[1] + ',' + sys.argv[2]
print data_str

s.sendto(data_str, ('<broadcast>', PORT))


#while 1:
#    data = 'HELLO\n'
#    s.sendto(data, ('<broadcast>', MYPORT))
#    time.sleep(2)
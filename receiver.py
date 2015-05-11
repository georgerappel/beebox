# Receive UDP packets transmitted by a broadcasting service
import sys
from socket import *
from OSC import OSCMessage
from OSC import OSCClient

PORT = 50000

client = OSCClient()
client.connect( ("127.0.0.1", 22243) )

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', PORT))

while 1:
    data, wherefrom = s.recvfrom(1500, 0)
    #print data
    strsplit = data.split(',')
    kind = strsplit[0]
    val  = strsplit[1] 
    print kind, val



    if   kind == 'TEMP':
    	client.send( OSCMessage("/shast/beebox/tmp", float(val)/100))
    elif kind == 'HUM':
    	client.send( OSCMessage("/shast/beebox/hum", float(val)/100))
    elif kind == 'LIGHT':
    	client.send( OSCMessage("/shast/beebox/lht", float(val)/1024))
    elif kind == 'MOIST':
    	client.send( OSCMessage("/shast/beebox/moi", float(val)/1024))

	#time.sleep(2)





    #sys.stderr.write(repr(wherefrom) + '\n')
    #sys.stdout.write('->' + data)

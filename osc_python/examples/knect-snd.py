#!/usr/bin/env python
from OSC import OSCClient, OSCMessage

client = OSCClient()
client.connect( ("localhost", 7110) )

client.send( OSCMessage("/gduarte/1", [1.0, 2.0, 3.0 ] ) )
client.send( OSCMessage("/gduarte/2", [2.0, 3.0, 4.0 ] ) )
client.send( OSCMessage("/gduarte/3", [2.0, 3.0, 3.1 ] ) )
client.send( OSCMessage("/gduarte/4", [3.2, 3.4, 6.0 ] ) )

client.send( OSCMessage("/quit") )


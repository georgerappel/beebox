#!/usr/bin/python
#-*- coding:utf-8 -*-#

import sys
import signal
import threading
from optparse import OptionParser
from OSC import OSCClient
from beemotion import BeeMotionDetec

def signal_handler(signal, frame):
        print 'You killed me!'
        sys.exit(0)


if __name__=="__main__":
    parser = OptionParser(usage="usage: %prog [options]",
                          version="%prog 0.1")
    parser.disable_interspersed_args()
    #parser.add_option('--sport', '-p', dest='port', type="string", help="Select the UDP boardcast port to be used")
    parser.add_option('--osc', '-s', dest='server', type="string", help="Point to OSC server")
    parser.add_option('--oport', '-o', dest='oscport', type="int", help="Server Port")

    
    (opts, remainder) = parser.parse_args()

    if opts.server is None:
        print 'You must point the server where data will be sent!'
        sys.exit(-1)

    
    if opts.oscport is None:
        print 'You must tell the port used on OSC server'
        sys.exit(-1)


    #if opts.port is None:
    #    print "Serial port not chosen"
    #    sys.exit(-1)



    client = OSCClient()
    client.connect( (opts.server, opts.oscport) )
    lock = threading.Lock()


    #client.send( OSCMessage("/gduarte/1", [1.0, 2.0, 3.0 ] ) )
    #client.send( OSCMessage("/gduarte/2", [2.0, 3.0, 4.0 ] ) )
    #client.send( OSCMessage("/gduarte/3", [2.0, 3.0, 3.1 ] ) )
    #client.send( OSCMessage("/gduarte/4", [3.2, 3.4, 6.0 ] ) )
    #client.send( OSCMessage("/quit") )
    threads = []
    
    motion = BeeMotionDetec(client, lock)
    #udp_data = YunData(client, opts.port, lock)

    threads.append(motion)
    #threads.append(udp_data)
    #udp_data.start()
    motion.start()

    while len(threads) > 0:
        try:
            # Join all threads using a timeout so it doesn't block
            # Filter out threads which have been joined or are None
            threads = [t.join(1) for t in threads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            print "Ctrl-c received! Sending kill to threads..."
            for t in threads:
                t.kill_received = True


    

import os
import sys
import serial
import time
from serial.tools import list_ports
import threading
from OSC import OSCMessage

class ArduinoSerial(threading.Thread):
	
	def __init__(self, osc, serialport, lock):		
		threading.Thread.__init__(self)
		self.kill_received = False
		self.lock = threading.Lock()
		self.serialport = serialport
		self.lock = lock
		self.osc = osc


		if self.serialport == None:
			print "Erro: No serial port"


		self.port = serial.Serial(serialport, baudrate=9600, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, timeout=1.0)
		print self.port

	def read(self):
		return self.port.readline()
		



	def run(self):
		while not self.kill_received:
			out = self.read()
			ary = out.replace("[", "").replace("]", "").split(",")
			if len(ary) > 2:
				light, moist, temp, humid = out.replace("[", "").replace("]", "").split(",")
				self.lock.acquire()
				self.osc.send( OSCMessage("/shast/beebox/hum", humid))
				self.osc.send( OSCMessage("/shast/beebox/lig", light))
				self.osc.send( OSCMessage("/shast/beebox/moi", moist))
				self.osc.send( OSCMessage("/shast/beebox/temp", temp))
	            
				self.lock.release()
				print light,moist,temp,humid
				time.sleep(1)
			else:
				print out		



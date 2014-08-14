import os
import sys
import serial
import time
from serial.tools import list_ports
import threading
from OSC import OSCMessage

class ArduinoSerial(threading.Thread):
	
	def __init__(self, os, serialport=None):		
		threading.Thread.__init__(self)
		self.kill_received = False
		self.lock = threading.Lock()
		self.serialport = serialport

		if self.serialport == None:
			print "Erro: No serial port"


		self.port = serial.Serial(serialport, baudrate=9600, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, timeout=1.0)
		print self.port

	def read(self):
		return self.port.readline()
		



	def run(self):
		while not self.kill_received:
			print self.read()
			time.sleep(1)
		



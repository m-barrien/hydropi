import RPi.GPIO as GPIO
from time import sleep
 

class RelayGPIO(object):
	"""docstring for RelayGPIO"""
	def __init__(self, channels):
		self.channels = channels
		self.status={}
		GPIO.setmode(GPIO.BCM)
		for chann in channels:
			GPIO.setup(chann, GPIO.OUT)
		self.relay_off()
	def relay_on(self, index=None):
		if index!= None:
			GPIO.output(self.channels[index], GPIO.LOW)
			self.status[self.channels[index]]= True
		else:
			GPIO.output(self.channels, GPIO.LOW) 
			for chn in self.channels:
				self.status[chn] = True
	def relay_off(self, index=None):
		if index != None:
			GPIO.output(self.channels[index], GPIO.HIGH)
			self.status[self.channels[index]]= False
		else:
			GPIO.output(self.channels, GPIO.HIGH) 
			for chn in self.channels:
				self.status[chn] = False
	def get_status(self):
		result =[]
		for chn in self.channels:
			result.append(self.status[chn])
		return result

	def cleanup(self):
		GPIO.cleanup( self.channels )


import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class SoilMeter(object):
	"""docstring for SoilMeter"""
	def __init__(self):
		# Create the I2C bus
		self.i2c = busio.I2C(board.SCL, board.SDA)

		# Create the ADC object using the I2C bus
		self.ads1 = ADS.ADS1115(self.i2c, address=0x48)
		self.ads2 = ADS.ADS1115(self.i2c, address=0x49)

		# Create single-ended input on channel 0
		self.channels = [AnalogIn(self.ads1, ADS.P0) , AnalogIn(self.ads1, ADS.P1) , AnalogIn(self.ads1, ADS.P2) , AnalogIn(self.ads1, ADS.P3) , AnalogIn(self.ads2, ADS.P0) , AnalogIn(self.ads2, ADS.P1) , AnalogIn(self.ads2, ADS.P2) , AnalogIn(self.ads2, ADS.P3)]
	def read_voltage(self,pin=None):
		if not pin:
			voltages = []
			for analog in self.channels:
				voltages.append(analog.voltage)
			return voltages
		else:
			return self.channels[pin].voltage

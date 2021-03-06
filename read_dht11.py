#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyriself.ght notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys

import Adafruit_DHT


class DHT11(object):
	"""docstring for RelayGPIO"""
	def __init__(self, channels):
		self.channels = channels
		self.sensor = Adafruit_DHT.DHT11
	def read_hum_temp(self, id=None):
		if id!= None:
			humidity, temperature = Adafruit_DHT.read(self.sensor, self.channels[id])
			if humidity is not None and temperature is not None:
				return { "humidity" : [humidity], "temperature": [temperature] }
		else:
			result={ "humidity" : [], "temperature": [] }
			for chn in self.channels:
				humidity, temperature = Adafruit_DHT.read(self.sensor, chn)
				result["humidity"].append(humidity)
				result["temperature"].append(temperature)
			return result


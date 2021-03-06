from time import sleep
from ads1115 import SoilMeter
from read_dht11 import DHT11
from relay_control import RelayGPIO

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

#Sensors
air = DHT11([17,27])
relayControl = RelayGPIO((23,24))
soil = SoilMeter()


relay_1_on = "/relay/1/on"
relay_2_on = "/relay/2/on"
relay_1_off = "/relay/1/off"
relay_2_off = "/relay/2/off"
relay_read = "/relay"
read_hum_temp = "/temp"
soil_read = "/soil"
read_all = "/"
routes=[relay_1_on ,relay_2_on ,relay_1_off ,relay_2_off ,relay_read ,read_hum_temp ,soil_read,read_all]

class SensorHTTPRequestHandler(BaseHTTPRequestHandler):
	def set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()
	def do_GET(self):
		self.set_headers()
		out={}
		if self.path in routes:
			if self.path == relay_1_on:
				relayControl.relay_on(index=0)
				out["relay"] = relayControl.get_status()
			elif self.path == relay_2_on:
				relayControl.relay_on(index=1)
				out["relay"] = relayControl.get_status()
			elif self.path == relay_1_off:
				relayControl.relay_off(index=0)	
				out["relay"] = relayControl.get_status()
			elif self.path == relay_2_off:
				relayControl.relay_off(index=1)
				out["relay"] = relayControl.get_status()
			elif self.path == relay_read:
				out = relayControl.get_status()
			elif self.path == read_hum_temp:
				out["air"] = air.read_hum_temp()
			elif self.path == soil_read:
				out["soil"] = soil.read_voltage()
			elif self.path == read_all:
				out["soil"] = soil.read_voltage()
				out["air"] = air.read_hum_temp()
				out["relay"] = relayControl.get_status()
				
			self.wfile.write(json.dumps(out).encode("utf-8"))
			


		else:
			self.send_error(404)
			self.send_header('Access-Control-Allow-Origin', '*')
			self.end_headers()


httpd = HTTPServer(('', 8888), SensorHTTPRequestHandler)

#httpd.socket = ssl.wrap_socket (httpd.socket, keyfile="crt/key.pem", certfile='crt/cert.pem', server_side=True)
try:
	httpd.serve_forever()
except KeyboardInterrupt as e:
	relayControl.cleanup()
	exit(0);
finally:
	relayControl.cleanup()
	pass





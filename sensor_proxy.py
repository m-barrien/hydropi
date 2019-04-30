from time import sleep
from ads1115 import SoilMeter
from read_dht11 import DHT11
from relay_control import RelayGPIO

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

#Sensors
air = DHT11([17])
relayControl = RelayGPIO((23,24))
soil = SoilMeter()


relay_1_on = "/relay/1/on"
relay_2_on = "/relay/2/on"
relay_1_off = "/relay/1/off"
relay_2_off = "/relay/2/off"
relay_read = "/relay"
read_hum_temp = "/temp"
soil_read = "/soil"
routes=[relay_1_on ,relay_2_on ,relay_1_off ,relay_2_off ,relay_read ,read_hum_temp ,soil_read]

class SensorHTTPRequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		print(self.path)
		if self.path in routes:
			if self.path == relay_1_on:
				relayControl.relay_on(index=0)
			elif self.path == relay_2_on:
				relayControl.relay_on(index=1)
			elif self.path == relay_1_off:
				relayControl.relay_off(index=0)	
			elif self.path == relay_2_off:
				relayControl.relay_off(index=1)
			elif self.path == relay_read:
				relayControl.get_status()
			elif self.path == read_hum_temp:
				air.read_hum_temp()
			elif self.path == soil_read:
				soil.read_voltage()

			self.send_response(200)
			self.send_header('Access-Control-Allow-Origin', '*')
			self.end_headers()

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





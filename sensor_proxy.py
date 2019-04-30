from time import sleep
from ads1115 import SoilMeter
from read_dht11 import DHT11
from relay_control import RelayGPIO


air = DHT11([17])
print(air.read_hum_temp())



relayControl = RelayGPIO((23,24))
relayControl.relay_on(index=1)
sleep(1)
relayControl.relay_on(index=0)


soil = SoilMeter()
print(soil.read_voltage())

relayControl.cleanup()


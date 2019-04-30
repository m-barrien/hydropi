from time import sleep
from ads1115 import SoilMeter
from relay_control import RelayGPIO

relayControl = RelayGPIO((23,24))
relayControl.relay_on(index=1)
sleep(1)
relayControl.relay_on(index=0)


soil = SoilMeter()
print(soil.read_voltage())

relayControl.cleanup()
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
RELAIS_1_GPIO = 23
RELAIS_2_GPIO = 24
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # out
sleep(3)
#GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
#GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # on
GPIO.cleanup( (RELAIS_1_GPIO, RELAIS_2_GPIO) )
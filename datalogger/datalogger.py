import json
import requests
from time import sleep
while True:
	r = requests.get('http://localhost:8888/', timeout=2)
	response = r.json()
	sleep(5)
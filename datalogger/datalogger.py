import json
import requests
import mysql.connector as mariadb
from time import sleep

mariadb_connection = mariadb.connect(host='localhost',user='dbuser', password='dbpass', database='hydrodb')
cursor = mariadb_connection.cursor()

insert_string = "INSERT INTO logs (relay1on, relay2on, soil1voltage, soil2voltage, soil3voltage, soil4voltage, soil5voltage, soil6voltage, soil7voltage, soil8voltage, humidity1, humidity2, temperature1, temperature2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
while True:
	r = requests.get('http://localhost:8888/', timeout=2)
	response = r.json()
	
	try:
		insert_input = (
			0 if response["relay"][0]== False else 1,
			0 if response["relay"][1]== False else 1,
			response["soil"][0],
			response["soil"][1],
			response["soil"][2],
			response["soil"][3],
			response["soil"][4],
			response["soil"][5],
			response["soil"][6],
			response["soil"][7],
			0.0 if response["air"]["humidity"][0] == None else response["air"]["humidity"][0],
			0.0 if response["air"]["humidity"][1] == None else response["air"]["humidity"][1],
			0.0 if response["air"]["temperature"][0] == None else response["air"]["temperature"][0],
			0.0 if response["air"]["temperature"][1] == None else response["air"]["temperature"][1],
			)
		cursor.execute(insert_string, insert_input)

		mariadb_connection.commit()
		sleep(5)
	except mariadb.Error as error:
		print("Error: {}".format(error))	
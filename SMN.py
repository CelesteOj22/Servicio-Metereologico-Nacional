import requests
import json
url='https://ws.smn.gob.ar/map_items/weather'
#args= {'nombre': 'Eduardo','curso':'python'}

response = requests.get(url)#, #params=args)
if response.status_code ==200: #si realiza la conexion
	#response_json=response.json() #es un diccionario??
	#print(response_json)
	response_json=json.loads(response.text)
	print(response_json)


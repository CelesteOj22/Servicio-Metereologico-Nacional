import requests
import json
url='https://ws.smn.gob.ar/map_items/weather'

response = requests.get(url)
if response.status_code ==200: #si realiza la conexion
	#response_json=response.json() #es un diccionario??
	#print(response_json)
	response_json=json.loads(response.text)
	a=input('Ingrese su peticion: ')
	for i in response_json:
		if (i)['province']==a:
			idj=i
			print(idj)
		else:
			continue
	#print((response_json[0])['name']) #son 217 registros


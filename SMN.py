#probabilidad de incendio forestal
import requests
import json
from SMNFunciones import *

url='https://ws.smn.gob.ar/map_items/weather'

response = requests.get(url) 
if response.status_code ==200: #procede si se establece la conexion
	response_json=json.loads(response.text) #guarda en una variable el contenido de la api que estamos consumiendo
	
	provl=ListaProv(response_json) #guarda la lista de provincias en la variable provl
	MostrarLista(provl) #muestra la lista

	p=input('Elija una Provincia: ') #
	
	prov=provl[int(p)] #busca la provincia en la lista correspondiente al indice ingresado p

	locl=ListaLoc(prov,response_json)
	MostrarLista(locl)
	l=input('Elija una localidad: ')
	loc=locl[int(l)]
	
	h,velv,t=Resultado(prov,loc,response_json)

	probabilidad(h,velv,t)

else:
	print('Conexion fallida! Intente nuevamente.')
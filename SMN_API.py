import requests
import json

#-----------------------Conexion-----------------------------
def conexion(url):
	response = requests.get(url) 
	if response.status_code ==200: #procede si se establece la conexion
		json=JSON(response)
		return json
	else:
		print('Conexion fallida! Intente nuevamente.')

def JSON(response):
		response_json=json.loads(response.text) #guarda en una variable el contenido de la api que estamos consumiendo
		return response_json
	
#-----------------------Armado de Listas-----------------------------
def ListaProv(response_json):#func de lista de provincia
	provl=list() #creamos la lista para almacenar las provincias 
	for i in response_json: #recorremos el diccionario

		if len(provl)==0: #verifica si hay elementos en la lista de provincias
			provl.append((i)['province']) #carga el primer elemento
			continue
		else:
			if (i)['province'] in provl: #evalua si la provincia ya se encuentra en la lista
				continue #sigue recorriendo el json
			else:
				provl.append((i)['province']) #si la provincia no se encuentra en la lista, 
				continue
	return provl
	
def ListaLoc(prov,response_json): #func de lista de localidades
	n=0 #contador para para señalizar el indice de cada localidad
	locl=list() #se crea la lista para almacenar las localidades
	for i in response_json:
		if (i)['province']==prov: #si la provincia en el json  es igual a la que se pasa por parametro (prov)
			locl.append((i)['name']) #se guarda en la lista la localidad
		else:
			continue
	return locl

def MostrarLista(lista):	
	n=0 #contador para señalizar el indice de cada provincia/localidad
	for i in lista:	#recorre la lista
		print(n,' ',lista[n]) #lista con las provincias/localidades que se pueden llegar a usar
		n=n+1
		continue

#-----------------------Extraccion de atributos de interes-----------------------------
def Clima(prov,loc,response_json):
	for i in response_json:
		if (i)['province']==prov and (i)['name']==loc:
			h=(i)['weather']['humidity'] #humedad
			velv=(i)['weather']['wind_speed'] #velocidad del viento
			t=(i)['weather']['temp'] #temperatura
		else:
			continue
	print('\n\nProvincia: ',prov,'\nLocalidad: ',loc,'\nHumedad: ',h,'\nVelocidad del Viento: ',velv,'\nTemperatura: ',t)
	return h,velv,t



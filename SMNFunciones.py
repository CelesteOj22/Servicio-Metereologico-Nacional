import requests
import json

def ListaProv(response_json):
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

	
def MostrarLista(lista):	
	n=0 #contador para señalizar el indice de cada provincia/localidad
	for i in lista:	#recorre la lista
		print(n,' ',lista[n]) #lista con las provincias/localidades que se pueden llegar a usar
		n=n+1
		continue
	
def ListaLoc(prov,response_json): #func de lista de localidades
	n=0 #contador para para señalizar el indice de cada localidad
	locl=list() #se crea la lista para almacenar las localidades
	for i in response_json:
		if (i)['province']==prov: #si la provincia en el json  es igual a la que se pasa por parametro (prov)
			locl.append((i)['name']) #se guarda en la lista la localidad
		else:
			continue
	return locl

def Resultado(prov,loc,response_json):
	for i in response_json:
		if (i)['province']==prov and (i)['name']==loc:
			h=(i)['weather']['humidity'] #humedad
			velv=(i)['weather']['wind_speed'] #velocidad del viento
			t=(i)['weather']['temp'] #temperatura
		else:
			continue
	print('\nProvincia: ',prov,'\nLocalidad: ',loc,'\nHumedad: ',h,'\nVelocidad del Viento: ',velv,'\nTemperatura: ',t)
	return h,velv,t

def tablaTemp(t): #Dependiendo del valor de la temperatura, le asigna un indice
	if t<10:
		it=2.5
	elif 10<=t<=11.9:
		it=5.0
	elif 12<=t<=13.9:
		it=7.5
	elif 14<=t<=15.9:
		it=10.5
	elif 16<=t<=17.9:
		it=12.0
	elif 18<=t<=19.9:
		it=15.5
	elif 20<=t<=21.9:
		it=17.5
	elif 22<=t<=23.9:
		it=20.0
	elif 24<=t<=25.9:
		it=22.5
	else:
		it=25.0
	return it

def tablaHume(h): #Dependiendo del valor de la humedad, le asigna un indice
	if h>80:
		ih=2.5
	elif 79>=h>=75:
		ih=5.0
	elif 74>=h>=70:
		ih=7.5
	elif 69>=h>=65:
		ih=10.5
	elif 64>=h>=60:
		ih=12.5
	elif 59>=h>=55:
		ih=15.0
	elif 54>=h>=50:
		ih=17.5
	elif 49>=h>=45:
		ih=20.0
	elif 44>=h>=40:
		ih=22.5
	else:
		ih=25.0
	return ih

def tablaVelv(velv): #Dependiendo del valor de la velocidad del viento, le asigna un indice
	if velv<3.0:
		ivelv=1.5
	elif 3.0<=velv<=5.9:
		ivelv=3.0
	elif 6.0<=velv<=8.9:
		ivelv=4.5
	elif 9.0<=velv<=11.9:
		ivelv=6.0
	elif 12.0<=velv<=14.9:
		ivelv=7.5
	elif 15.0<=velv<=17.9:
		ivelv=9.0
	elif 18.0<=velv<=20.9:
		ivelv=10.5
	elif 21.0<=velv<=23.9:
		ivelv=12.0
	elif 24.0<=velv<=26.9:
		ivelv=13.5
	else:
		ivelv=15.0
	return ivelv

def probabilidad(h,velv,t):
	temperatura=tablaTemp(t)
	humedad=tablaHume(h)
	velocviento=tablaVelv(velv)
	ind=temperatura+humedad+velocviento

	#print("temp",temperatura,"	humedad:",humedad,"	 velocviento",velocviento,"	indice",ind)

	if 0<=ind<=16:
		prob="Leve"
	elif 17<=ind<=32:
		prob="Moderado"
	elif 33<=ind<=48:
		prob="Alto"
	elif  49<=ind<=65:
		prob="Extremo"
	else:
		print("\nHa ocurrido un error: Indice fuera de los parametros establecidos.")
	return print("\nLa probabilidad de incendio forestal es: ",prob)


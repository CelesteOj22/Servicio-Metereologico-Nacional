import requests
import json
url='https://ws.smn.gob.ar/map_items/weather'

response = requests.get(url)
if response.status_code ==200: #procede si se establece la conexion
	response_json=json.loads(response.text) #guarda en una variable el contenido de la api que estamos consumiendo
	provl=['Corrientes','Entre Rios','Chaco','Misiones'] #lista con las provincias que se pueden llegar a usar
	prov=provl[0] #se guarda corrientes en p
	#a=input('0:Corrientes. 1:Entre Rios. 2:Chaco. 3:Misiones. Ingrese el numero correspondiente: ')
	#prov=provl[a]
	for i in response_json:
		if (i)['province']==prov:
			l=(i)['name'] #localidad
			h=(i)['weather']['humidity'] #humedad
			p=(i)['weather']['pressure'] #presion
			v=(i)['weather']['visibility'] #visibilidad
			velv=(i)['weather']['wind_speed'] #velocidad del viento
			d=(i)['weather']['description'] #descripcion del clima
			t=(i)['weather']['temp'] #temperatura
			w=(i)['weather']['wing_deg']
			td=(i)['weather']['tempDesc']
			print('\nProvincia: ',prov,'\nLocalidad: ',l,'\nHumedad: ',h,'\nPresion: ',p,'\nVisibilidad: ',v,'\nVelocidad del Viento: ',velv,'\nDescripcion: ',d,'\nTemperatura: ',t)
		else:
			continue
	#son 217 registros
else:
	print('Conexion fallida! Intente nuevamente')

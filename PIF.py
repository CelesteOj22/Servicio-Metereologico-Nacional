#Probabilidad de incendio forestal
import SMN_API as API
import CalculoProbIncendio

#-----------Conexion con la API y almacenado de diccionario
url='https://ws.smn.gob.ar/map_items/weather' #direccion en la que se encuentra la API del Servicio Metereologico Nacional
json=API.conexion(url) #Se realiza la conexion con la API y se guarda su diccionario en una variable "json" para su manejo

#-----------Seleccion de Provincia
print("\nProvincias:\n")
API.MostrarLista(API.ListaProv(json)) #muestra la lista de provincias

p=input('\nElija una Provincia: ') 
prov=API.ListaProv(json)[int(p)] #busca la provincia en la lista correspondiente al indice ingresado p

#-----------Seleccion de Localidad
print("\nLocalidades de ",prov,"\n")
API.MostrarLista(API.ListaLoc(prov,json)) #muestra la lista de localidades

l=input('\nElija una localidad: ')
loc=API.ListaLoc(prov,json)[int(l)]

#-----------Resultado de Probabilidad de Incendio Forestal
h,velv,t=API.Clima(prov,loc,json) #almacena la humedad,temperatura y velocidad del viento de la localidad solicitada
CalculoProbIncendio.probabilidad(h,velv,t) #clasifica la probabilidad de incendio forestal


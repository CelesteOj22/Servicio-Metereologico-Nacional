#Probabilidad de incendio forestal
from SMN_API import *
from CalculoProbIncendio import *

#-----------Conexion con la API y almacenado de diccionario
url='https://ws.smn.gob.ar/map_items/weather' #direccion en la que se encuentra la API del Servicio Metereologico Nacional
json=conexion(url) #Se realiza la conexion con la API y se guarda su diccionario en una variable "json" para su manejo

#-----------Seleccion de Provincia
print("\nProvincias:\n")
MostrarLista(ListaProv(json)) #muestra la lista de provincias

p=input('\nElija una Provincia: ') 
prov=ListaProv(json)[int(p)] #busca la provincia en la lista correspondiente al indice ingresado p

#-----------Seleccion de Localidad
print("\nLocalidades de ",prov,"\n")
MostrarLista(ListaLoc(prov,json)) #muestra la lista de localidades

l=input('\nElija una localidad: ')
loc=ListaLoc(prov,json)[int(l)]

#-----------Resultado de Probabilidad de Incendio Forestal
h,velv,t=Clima(prov,loc,json) #almacena la humedad,temperatura y velocidad del viento de la localidad solicitada
probabilidad(h,velv,t) #clasifica la probabilidad de incendio forestal


import math

#-----------------------Calculo de probabilidad de incendio forestal-----------------------------
def probabilidad(h,velv,t):
    ind=tablaTemp(t)+tablaHume(h)+tablaVelv(velv)

    #print("temp",tablaTemp(t),"    humedad:",tablaHume(h),"     velocviento",tablaVelv(velv)," indice",ind)

    if 0<=ind<=16:
        prob="Leve"
    elif 17<=ind<=32:
        prob="Moderado"
    elif 33<=ind<=48:
        prob="Alto"
    elif  49<=ind<=65:
        prob="Extremo"
    else:
        print("\nHa ocurrido un error: Indice fuera de los parametros establecidos")
    return print("\nLa probabilidad de incendio forestal es: ",prob)

#-----------------------Asignacion de valores/tablas-----------------------------

def tablaTemp(t):  # Dependiendo del valor de la temperatura, le asigna un indice
    valoresIndice = [2.5, 5.0, 7.5, 10.5, 12.0, 15.5, 17.5, 20.0, 22.5, 25]
    index = 0

    if t > 26:
        index = 9
    elif t >= 10:
        index = math.floor((t - 10) / 2) + 1
    it = valoresIndice[index]

    return it


def tablaHume(h):  # Dependiendo del valor de la humedad, le asigna un indice
    valoresIndice = [2.5, 5.0, 7.5, 10.5, 12.5, 15.0, 17.5, 20.0, 22.5, 25]
    index = 9

    if h > 80:
        index = 0
    elif h > 40:
        index = math.ceil(((h - 80) * -1) / 5)
    ih = valoresIndice[index]

    return ih


def tablaVelv(velv):  # Dependiendo del valor de la velocidad del viento, le asigna un indice
    ivelv = 1

    if velv > 27:
        ivelv = 10
    elif velv >= 3:
        ivelv += math.floor(velv / 3)
    ivelv *= 1.5

    return ivelv

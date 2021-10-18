import csv
from pprint import pprint
from collections import Counter
#ejercicio 3.18

def leer_parque(nombre_archivo, parque):
    park = parque.upper()
    park_list = []
    with open(nombre_archivo, 'rt', encoding=('utf8')) as f:
        file = csv.reader(f)
        header = next(file)
        for row in file:
            dicc = dict(zip(header, row))
            for k in dicc:
                if dicc[k].isnumeric():
                    dicc[k] = float(dicc[k])
            if dicc['espacio_ve'] == park:
                park_list.append(dicc)
    return park_list, park

#ejercicio 3.22

def obtener_inclinaciones(lista_arboles, especie):
    inclinacion = []
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            inclinacion.append(i['inclinacio'])      
    return inclinacion, especie
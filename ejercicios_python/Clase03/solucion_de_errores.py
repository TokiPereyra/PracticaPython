#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
'''Encontré el error en la linea 15 ya que al comprobar que la letra del indice no era 'a' directamente
devolvía false sin comprobar el resto de las letras en la cadena'''
'''Para solucionarlo, moví la suma del i al inicio del else y agregé un continue moviendo el 'return False' fuera del bucle while.'''
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    print(expresion[0])
    while i < n:
        if expresion[i] == 'a':
            return True
        else:
            i += 1
            continue
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: Encontré errores en las lineas 33, 36, 37 y 40. En la linea 33, a la definicion de la funcion le faltaban dos puntos ':'.
#En la linea 36, a la declaracion del bucle le faltaban los dos puntos ':'
#En la linea 37, a la declaracion del if la comprobacion de igualdad solo tenia un signo = siendo que debe llevar dos ==, ademas le faltaban los dos puntos ':' 
#En la linea 40, la palabra False estaba mal escrita.
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: Encontré el error y lo corregí en la línea 51 añadiendo un if para pasar a String la cadena que ingresaran aunque fuera un número.

def tiene_uno(expresion):
    if expresion != '':
        expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)


#%%
#Ejercicio 3.4. Función suma()
#Comentario: Encontré el error en la línea 74 ya que la funcion se ejecutaba correctamente pero no devolvia ningun valor. Agregé un return.

def suma(a,b):
    c = a + b
    return c
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


#%%
#Ejercicio 3.5. Función leer_camion()
#Comentario: Encontré el error en la linea 100 ya que siempre era el mismo append asi que comenté la linea de declaracion de 'registro' y la declaré directamente dentro del 'for'

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    #registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas: 
            registro = {
            encabezado[0] : fila[0],
            encabezado[1] : int(fila[1]),
            encabezado[2] : float(fila[2])
            }
            camion.append(registro)
    return camion

camion = leer_camion('Data/camion.csv')
pprint(camion)
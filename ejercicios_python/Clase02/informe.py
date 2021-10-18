import csv

def leer_camion(nombre_archivo):
    info_camion = []
    costo = 0.0

    with open(nombre_archivo, 'rt') as file:
        lineas = csv.reader(file)
        next(lineas)

        for linea in lineas:
            lote = (linea[0], int(linea[1]), float(linea[2]))
            info_camion.append(lote)
        
        for linea in info_camion:
            costo = costo + linea[1] * linea[2]

    return costo


def leer_precios(nombre_archivo):
    precio_cajones = {}
    costo = 0.0

    with open(nombre_archivo, 'rt') as file:
        lineas = csv.reader(file)

        for linea in lineas:
            if linea != []:
                precio_cajones[linea[0]] = float(linea[1])
                costo = costo + float(linea[1])

    return costo


costo_camion = leer_camion('Data\camion.csv')
ventas = leer_precios('Data\precios.csv')

print('El camion costó: ', costo_camion)
print('Lo recaudado por las ventas fue: ', ventas)

if ventas < costo_camion:
    print('La perdida fue de: ', ventas - costo_camion)
else:
    print('La ganancia fue de: ', ventas - costo_camion)

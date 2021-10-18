import csv
import sys

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)

    headers = next(rows)

    total = 0.0

    for row in rows:
        total = total + (float(row[1]) * float(row[2]))

    return total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
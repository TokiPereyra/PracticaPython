import csv

def costo_camion(place):
    f = open(place)
    rows = csv.reader(f)

    headers = next(rows)

    total = 0.0

    for row in rows:
        total = total + (float(row[1]) * float(row[2]))

    return total

costo = costo_camion('Data\camion.csv')
print('Costo total: ', costo)
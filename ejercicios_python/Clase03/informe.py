import csv

def leer_camion(ruta_archivo):
    camion = []
    with open(ruta_archivo, 'rt') as f:
        rows = csv.reader(f)
        header = (next(rows))
        costo_total = 0.0
        for i, row in enumerate(rows, start = 1):
            record = dict(zip(header, row))
            try:
                nbox =  int(record['cajones'])
                price = float(record['precio'])
                costo_total += nbox * price
            except AttributeError:
                print (f'Fila {i}: no se puede interpretar: {row}')
            camion.append(record)
        return costo_total, camion


def leer_precios(ruta_archivo):
    precios = {}
    with open(ruta_archivo, 'rt') as f:
        file = csv.reader(f)
        for line in file:
            try:
                precios[line[0]] = line[1]
            except IndexError:
                print('Error')          
        return precios

def balance(precios_venta, costo_camion):
    costo, camion = leer_camion(costo_camion)
    precios = leer_precios(precios_venta)
    venta = 0.0
    for i in camion:
        if i['nombre'] in precios.keys():
            venta += float(precios[i['nombre']])*int(i['cajones'])  
    
    resto = round(venta - costo, 2)
    
    print(f'''
          Costo del camión:\t\t ${costo}
          Ventas:\t\t\t ${venta}
          Resto:\t\t\t ${resto}
          ''')
    return resto, venta, costo
    
    
g = balance('Data/precios.csv', 'Data/fecha_camion.csv')
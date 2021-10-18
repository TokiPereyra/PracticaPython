def buscar_precio(fruta):
    with open('Data\precios.csv', 'rt') as f:
        for line in f:
            fruit = line.split(',')
            if fruit[0] == fruta:
                print('El precio de un cajón de ', fruta, ' es: ', fruit[1])

print(buscar_precio('Tomate'))
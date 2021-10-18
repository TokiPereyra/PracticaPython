

def diccionario_geringoso(lista):
    diccionario = {}
    for i in lista:
        diccionario[i] = traduccion_geringoso(i)
    return diccionario


def traduccion_geringoso(palabra):
    traduccion = ''
    for i in palabra:
        if i in 'aeiou':
            traduccion = traduccion + i + 'p' + i
        else:
            traduccion = traduccion + i
    return traduccion

lista = ['banana', 'manzana', 'mandarina']

print(diccionario_geringoso(lista))



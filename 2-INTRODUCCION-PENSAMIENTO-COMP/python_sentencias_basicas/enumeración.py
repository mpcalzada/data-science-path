objetivo = int(input('Escoge un entero'))
respuesta = 0

while respuesta ** 2 < objetivo:
    respuesta += 1

if respuesta ** 2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'No se encontro una raiz cuadrada para {objetivo}')

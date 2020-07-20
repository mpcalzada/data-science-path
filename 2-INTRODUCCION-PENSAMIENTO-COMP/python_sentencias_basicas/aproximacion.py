objetivo = int(input('Escoge un numero'))
epsilon = 0.001
paso = epsilon ** 2
respuesta = 0.0

while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    print(abs(respuesta ** 2 - objetivo), respuesta)
if abs(respuesta ** 2 - objetivo) >= epsilon:
    print(f'No se econtró raiz cuadrada para {objetivo}')
else:
    print(f'La raiz cuadra de {objetivo} es {respuesta}')

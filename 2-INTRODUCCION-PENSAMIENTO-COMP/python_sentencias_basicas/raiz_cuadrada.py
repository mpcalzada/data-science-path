def busqueda_binaria(target, epsilon=0.01):
    min_limit = 0.0
    max_limit = max(1.0, target)
    response = (max_limit + min_limit) / 2

    while abs(response ** 2 - target) >= epsilon:
        print(f'alto: {max_limit}, bajo: {min_limit}, respuesta: {response}')
        if response ** 2 < target:
            min_limit = response
        else:
            max_limit = response

        response = (max_limit + min_limit) / 2

    print(f'La raiz cuadra de {target} es {response}')


def aproximacion(target, epsilon=0.01):
    paso = epsilon ** 2
    respuesta = 0.0

    while abs(respuesta ** 2 - target) >= epsilon and respuesta <= target:
        respuesta += paso
        print(abs(respuesta ** 2 - target), respuesta)
    if abs(respuesta ** 2 - target) >= epsilon:
        print(f'No se econtró raiz cuadrada para {target}')
    else:
        print(f'La raiz cuadra de {target} es {respuesta}')


def enumeracion(target):
    respuesta = 0

    while respuesta ** 2 < target:
        respuesta += 1

    if respuesta ** 2 == target:
        print(f'La raiz cuadrada de {target} es {respuesta}')
    else:
        print(f'No se encontro una raiz cuadrada para {target}')


def main():
    method = int(input(
        f'Escoge un metodo: \n'
        f'[0] enumeracion exhahustiva\n'
        f'[1] Aproximacion\n'
        f'[2] Busqueda Binaria\n'
    ))
    objetivo = int(input("Escribe el objetivo: "))

    algorithm = {
        0: enumeracion,
        1: aproximacion,
        2: busqueda_binaria
    }

    algorithm[method](objetivo)


if __name__ == '__main__':
    main()

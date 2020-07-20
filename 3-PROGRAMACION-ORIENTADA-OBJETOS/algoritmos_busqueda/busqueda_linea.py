import random


def busqueda_lineal(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return True

    return False


if __name__ == '__main__':
    tamaño_lista = int(input('Tamaño de la lista: '))
    objetivo = int(input('Numero por buscar: '))
    lista = [random.randint(0, 100) for i in range(tamaño_lista)]

    encontrado = busqueda_lineal(lista, objetivo)

    print(f'El numero {objetivo} {"fue" if encontrado else "NO fue"} encontrado en la lista: {lista}')

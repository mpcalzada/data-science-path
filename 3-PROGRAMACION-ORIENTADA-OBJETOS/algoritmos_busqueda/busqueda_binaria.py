import random


def busqueda_binaria(lista, inicio, fin, objetivo):
    print(f'Buscando el objetivo {objetivo} entre {lista[inicio]} y {lista[fin - 1]}')
    if inicio > fin:
        return False

    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, inicio, medio - 1, objetivo)
    else:
        return busqueda_binaria(lista, medio + 1, fin, objetivo)


if __name__ == '__main__':
    tamaño_lista = int(input('Tamaño de la lista: '))
    objetivo = int(input('Numero por buscar: '))
    lista = sorted([random.randint(0, 100) for i in range(tamaño_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(f'El numero {objetivo} {"fue" if encontrado else "NO fue"} encontrado en la lista: {lista}')

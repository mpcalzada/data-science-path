import random


def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:  # O(n) * O(n - i -1) = O(n) * O(n) = O(n ** 2)
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


if __name__ == '__main__':
    tamano_lista = int(input('Tamaño de la lista: '))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    print(f'La lista desordenada es: {lista}')

    ordenada = ordenamiento_burbuja(lista)

    print(f'La lista ordenada es: {ordenada}')

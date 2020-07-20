import random


def ordenamiento_por_insercion(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice
        print(f'Indice {indice} valor actual {valor_actual}')

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            print(f'Posicion {posicion_actual} anterior {lista[posicion_actual - 1]} valor actual {valor_actual}')
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
        print(lista)

    return lista


if __name__ == '__main__':
    tamano_lista = int(input('Tamaño de la lista: '))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    print(f'La lista desordenada es: {lista}')

    ordenada = ordenamiento_por_insercion(lista)

    print(f'La lista ordenada es: {ordenada}')

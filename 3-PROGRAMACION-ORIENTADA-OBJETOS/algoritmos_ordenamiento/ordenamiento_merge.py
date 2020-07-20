import random


def ordenamiento_merge(lista):
    if len(lista) > 1:
        medio = len(lista) // 2

        izquierda = lista[:medio]
        derecha = lista[medio:]

        print('*' * 20)
        print(f'Lista: {lista} dirección: {id(lista)}')
        print(f'Izquierda: {izquierda} dirección: {id(izquierda)}')
        print(f'Derecha: {derecha} dirección: {id(derecha)}')

        ordenamiento_merge(izquierda)
        ordenamiento_merge(derecha)

        i = 0
        j = 0
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        return lista


if __name__ == '__main__':
    tamano_lista = int(input('Tamaño de la lista: '))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    print(f'La lista desordenada es: {lista} con id: {id(lista)}')
    print('-' * 40)

    ordenada = ordenamiento_merge(lista)

    print('-' * 40)
    print(f'La lista ordenada es: {ordenada} con id: {id(lista)}')

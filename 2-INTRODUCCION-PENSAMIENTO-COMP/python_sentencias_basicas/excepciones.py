def divide_elementos(lista, divsor):
    try:
        return [i / divsor for i in lista]
    except Exception as e:
        print(e)
        return lista


lista = [1, 2, 3]
divisor = 0

print(divide_elementos(lista, divisor))

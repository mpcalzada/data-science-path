def pares(end=100):
    return range(0, end, 2)


def nones(end=100):
    return range(1, end, 2)


def main():
    method = int(input("Selecciona el metodo (0 o 1): "))
    max_value = int(input("Selecciona el valor maximo de iteracion: "))
    methods = (pares, nones)

    method_range = methods[method](max_value)

    for i in method_range:
        print(i)


if __name__ == '__main__':
    main()

def factorial(number):
    """ Calculca el factorial de number

    :param number: Entero mayor a 0
    :return: Factorail de numero
    """
    if number == 1:
        return 1
    return number * factorial(number - 1)


def main():
    number = int(input("Ingresar el numero que se desea calcular: "))
    calc = factorial(number)

    print(f'El factorial de {number} es {calc}')


if __name__ == '__main__':
    main()

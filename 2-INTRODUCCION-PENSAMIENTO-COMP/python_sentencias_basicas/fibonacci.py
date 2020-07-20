def fibonacci(number):
    print(f'Evaluando: {number}')
    if number == 1 or number == 0:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


def main():
    number = int(input("Ingresa un numero: "))
    result = fibonacci(number)

    print(f'El resultado de fibonacci para {number} es {result}')


if __name__ == '__main__':
    main()

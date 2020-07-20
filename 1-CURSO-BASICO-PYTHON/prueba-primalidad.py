def es_primo(numero):
    if numero < 2:
        return False
    for i in range(1, numero):
        if (numero % 2) == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input('Ingrese un numero: '))
    print(f'El numero {n} {"es primo" if es_primo(n) else "no es primo"}')

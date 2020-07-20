import time


def factorial(n):
    resultado = 1

    while n > 1:
        resultado *= n
        n -= 1

    return resultado


def factorial_r(n):
    if n == 1:
        return n

    return n * factorial_r(n - 1)


if __name__ == '__main__':
    n = 200000

    inicio = time.time()
    factorial(n)
    fin = time.time()
    print(fin - inicio)

    inicio = time.time()
    factorial(n)
    fin = time.time()
    print(fin - inicio)

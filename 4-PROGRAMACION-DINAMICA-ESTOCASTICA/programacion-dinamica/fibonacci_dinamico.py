def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_dinamico(n, memo={}):
    print(f'fibonacci_dinamico({n}) | Memo(ID): {id(memo)} | Value: {memo}')
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado
        return resultado


if __name__ == '__main__':
    numero = int(input('Ingresa un valor: '))
    print(fibonacci_dinamico(numero))

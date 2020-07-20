def morral(tamaño, pesos, valores, n):
    if n == 0 or tamaño == 0:
        return 0
    if pesos[n - 1] > tamaño:
        return morral(tamaño, pesos, valores, n - 1)
    return max(
        valores[n - 1] + morral(tamaño - pesos[n - 1], pesos, valores, n - 1),
        morral(tamaño, pesos, valores, n - 1)
    )


if __name__ == '__main__':
    respuesta = 0
    for i in range(10):
        print(i)
    valores = [60, 100, 180]
    pesos = [10, 20, 30]
    tamano_morral = 30
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)

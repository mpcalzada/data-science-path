import random


def adivina():
    numero = random.randint(1, 100)
    vidas = 10
    while vidas > 0:
        vidas -= 1
        numero_ingresado = int(input('Ingresa un numero: '))
        if numero_ingresado == numero:
            print(f'¡Ganaste! El numero es {numero}')
            break
        elif numero_ingresado > numero:
            print('Elige un numero más pequeño')
        else:
            print('Elige un numero más grande')
    if vidas == 0:
        print(f'Upsss, has perdido. Vuelve a intentar, el numero era {numero}')


if __name__ == '__main__':
    adivina()

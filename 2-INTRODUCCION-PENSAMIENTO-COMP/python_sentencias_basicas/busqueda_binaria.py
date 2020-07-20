target = int(input('Chose one number: '))
epsilon = 0.00001
min_limit = 0.0
max_limit = max(1.0, target)
response = (max_limit + min_limit) / 2

while abs(response ** 2 - target) >= epsilon:
    print(f'alto: {max_limit}, bajo: {min_limit}, respuesta: {response}')
    if response ** 2 < target:
        min_limit = response
    else:
        max_limit = response

    response = (max_limit + min_limit) / 2

print(f'La raiz cuadra de {target} es {response}')

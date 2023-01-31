#exercicio 1
import math
try:
    numero = float(input('Digite um numero: '))
    print(f'{math.sqrt(numero)}')
    if numero < 0:
        raise ValueError
except ValueError as erro:
    print(f'{erro}, Escolha um numero valido')

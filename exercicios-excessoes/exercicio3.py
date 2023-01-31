#exercicio 3

try:
    numero = int(input('digite um numero: '))
    print(numero)
except ValueError:
    print('esse valor é inválido, digite um valor válido')

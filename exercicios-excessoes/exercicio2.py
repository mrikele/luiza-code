#exercício 2
try:
    numerador = float(input('Numerador: '))
    denominador = float(input('Denominador: '))
    divisao = numerador/denominador
    print(divisao)
    if denominador == 0:
        raise ZeroDivisionError
except ZeroDivisionError as error:
    print(error, 'denominador igual a 0, digite um numero valido')

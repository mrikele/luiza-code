#exercicio 6

try:
    n1 = float(input('insira um número: '))
    n2 = float(input('insira outro número: '))
    result = n1/n2
    print('resultado: {:.2f}'.format(resultado))

except ValueError:
    print('isso nao é um numero')
except ZeroDivisionError:
    print('divisão por 0 indeterminada')
except:
    print('algo deu errado')

# retorno: NameError

    

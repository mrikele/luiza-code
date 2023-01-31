try:
    file = open('file.txt', 'r')
    file.write('Exemplo de texto')
except IOError:
    print('Não foi possível escrever no arquivo.')
finally:
    file.close()

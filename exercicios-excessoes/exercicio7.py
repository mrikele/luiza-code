# exercicio 7
try: 
  file = open('file.txt', 'r')
  file_lines = file.readline()
  file.close()
except FileNotFoundError: 
  print('arquivo nao encontrado')

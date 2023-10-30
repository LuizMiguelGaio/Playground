N = int(input())

minuto = (N%3600)//60

hora = (minuto%3600)//60

segundo = (N%3600)%60


print(f'{hora}:{minuto}:{segundo}')

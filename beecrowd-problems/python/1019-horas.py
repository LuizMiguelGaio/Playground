N = int(input())

hora = N // 3600  
minuto = (N % 3600) // 60  
segundo = N % 60  

#print(f'{hora}:{minuto}:{segundo}')
print(hora, minuto, segundo, sep=':') #Só aceitou a resposta com a função 'sep'
N = int(input())

anos = N // 365 #divisão inteira por pela quantidade de dias que tem 1 anos
meses = (N%365) // 30 #Resultado do resto da divisão de 'anos' dividido inteiramente pela quantidade de dias que tem o mês  
dias = (N%365) % 30 #resto do resto que sao os dias

saida = f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)' #comecei a usar fString, uma maravilha

print(saida)


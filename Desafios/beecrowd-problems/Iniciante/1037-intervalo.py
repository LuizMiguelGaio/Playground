intervalos = ([0,25], [25,50], [50,75], [75,100])
numero = float(input())
for intervalo in intervalos:
    if numero >= intervalo[0] and numero <= intervalo[1]: 
        print(f'Intervalo {intervalo}') #Ainda não possuo conhecimento pra tirar os espaços na resposta, ela sai ex: [0, 25] e eu preciso [0,25]
        break
    else:
        print('Fora de Intervalo')

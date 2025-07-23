n = float(input())

if 0 <= n <= 1000000.00:
    nota100 = n // 100
    resto = n % 100
    nota50 = resto // 50
    resto = resto % 50
    nota20 = resto // 20
    resto = resto % 20
    nota10 = resto // 10
    resto = resto % 10
    nota5 = resto // 5
    resto = resto % 5
    nota2 = resto // 2
    resto = resto % 2
    moeda1 = resto // 1
    resto = resto % 1
    moeda50 = resto // 0.50
    resto = resto % 0.50
    moeda25 = resto // 0.25
    resto = resto % 0.25
    moeda10 = resto // 0.10
    resto = resto % 0.10
    moeda05 = resto // 0.05
    resto = resto % 0.05
    moeda01 = resto / 0.01
    

imprimiNota100 = f'{int(nota100)} nota(s) de R$ 100.00'
imprimiNota50 = f'{int(nota50)} nota(s) de R$ 50.00'
imprimiNota20 = f'{int(nota20)} nota(s) de R$ 20.00'
imprimiNota10 = f'{int(nota10)} nota(s) de R$ 10.00'
imprimiNota5 = f'{int(nota5)} nota(s) de R$ 5.00'
imprimiNota2 = f'{int(nota2)} nota(s) de R$ 2.00'
imprimiMoeda1 = f'{int(moeda1)} moeda(s) de R$ 1.00'
imprimiMoeda50 = f'{int(moeda50)} moeda(s) de R$ 0.50'
imprimiMoeda25 = f'{int(moeda25)} moeda(s) de R$ 0.25'
imprimiMoeda10 = f'{int(moeda10)} moeda(s) de R$ 0.10'
imprimiMoeda5 = f'{int(moeda05)} moeda(s) de R$ 0.05'
imprimiMoeda01 = f'{round(moeda01)} moeda(s) de R$ 0.01'

print('NOTAS:')
print(imprimiNota100)
print(imprimiNota50)
print(imprimiNota20)
print(imprimiNota10)
print(imprimiNota5)
print(imprimiNota2)
print('MOEDAS:')
print(imprimiMoeda1)
print(imprimiMoeda50)
print(imprimiMoeda25)
print(imprimiMoeda10)
print(imprimiMoeda5)
print(imprimiMoeda01)





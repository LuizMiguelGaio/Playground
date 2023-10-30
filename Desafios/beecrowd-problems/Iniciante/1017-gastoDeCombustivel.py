velocidade_Auto = 12
tempo = int(input())
velocidade_Media = int(input())

distancia_percorrida = tempo*velocidade_Media
consumo = distancia_percorrida/velocidade_Auto

print(format(consumo,'.3f'))
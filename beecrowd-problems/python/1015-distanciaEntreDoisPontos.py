
import math

x1, y1 = map(float,input().split())
x2, y2 = map(float,input().split())

#na raiz quadrada eu fiz (((x2-x1)**2)+((y2-y1)**2))**1/2 mas não fucionou
distancia = (((x2-x1)**2)+((y2-y1)**2))
#decidi usar a biblioteca math, pq se tem é pra usar né
resultado = math.sqrt(distancia)
print(format(resultado,".4f"))

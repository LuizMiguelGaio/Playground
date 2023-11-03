'''a, b, c = map(float, input().split())

delta = (b**2) - 4*a*c

if delta < 0:
    print('Impossivel calcular')
else:
    if delta == 0:
        x1 = (-b + delta ** 0.5) / (2*a) #Elevar um numero a 0.5 é a mesma que coisa que raiz quadrada
        print('R1 =', format(x1, '.5f'))
    else:
        x1 = (-b + delta ** 0.5) / (2*a)
        x2 = (-b - delta ** 0.5) / (2*a)
        print('R1 =',format(x1,'.5f'))
        print('R2 =',format(x2,'.5f'))'''

import math #usando biblioteca math

A, B, C = map(float, input().split())
delta = math.pow(B, 2) - 4*A*C 
if delta < 0 or A == 0: 
    print("Impossivel calcular")
else: 
    r1 = (-B + delta ** 0.5) / (2*A)
    r2 = (-B - delta ** 0.5) / (2*A) 
    print("R1 = %.5f" % (r1)) 
    print("R2 = %.5f" % (r2))
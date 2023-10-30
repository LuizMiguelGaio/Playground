a, b, c = map(float, input().split()) 

pi = 3.14159

areaTriangulo = (a*c)/2
areaCirculo = pi*c**2
areaTrapezio = ((a+b)*c)/2
areaQuadrado = b*b
areaRetangulo = a*b

print("TRIANGULO:", format(areaTriangulo,'.3f'))
print("CIRCULO:", format(areaCirculo,'.3f'))
print("TRAPEZIO:", format(areaTrapezio,'.3f'))
print("QUADRADO:", format(areaQuadrado,'.3f'))
print("RETANGULO:", format(areaRetangulo,'.3f'))
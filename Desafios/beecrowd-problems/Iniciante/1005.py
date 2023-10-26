a = float(input())
b = float(input())
nota1 = a*3.5
nota2 = b*7.5
media = (nota1+nota2)/11

if media > 10.0:
    media = 10.0

media_format = "%.5" % media

print("MEDIA =", media_format)



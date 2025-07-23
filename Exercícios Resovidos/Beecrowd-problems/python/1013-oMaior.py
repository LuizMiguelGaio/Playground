a, b, c = map(int, input().split())

maiorAB = ((a+b)+abs(a-b))/2

if maiorAB > c :
    maior = maiorAB
else :
    maior = c

print(format(maior,'.0f'), "eh o maior")
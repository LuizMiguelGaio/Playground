N = int(input())

if 0 < N < 1000000 :
    cedula100 = N//100
    resto = N%100

    cedula50 = resto//50
    resto = resto%50

    cedula20 = resto//20
    resto = resto%20

    cedula10 = resto//10
    resto = resto%10

    cedula5 = resto//5
    resto = resto%5

    cedula2 = resto//2
    resto = resto%2

    cedula1 = resto//1

    print(N)
    print(cedula100, "nota(s) de R$ 100,00")
    print(cedula50, "nota(s) de R$ 50,00")
    print(cedula20, "nota(s) de R$ 20,00")
    print(cedula10, "nota(s) de R$ 10,00")
    print(cedula5, "nota(s) de R$ 5,00")
    print(cedula2, "nota(s) de R$ 2,00")
    print(cedula1, "nota(s) de R$ 1,00")
else:
    print("N é um valor muito alto ou muito baixo.")

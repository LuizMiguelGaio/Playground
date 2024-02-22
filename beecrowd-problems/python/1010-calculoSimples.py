#Lendo os valores lado a lado
cod1, num1, und_valor1 = input().split()
cod2, num2, und_valor2 = input().split()

#atribuindo tipo numérico
cod1, num1, und_valor1 = int(cod1), int(num1), float(und_valor1)
cod2, num2, und_valor2 = int(cod2), int(num2), float(und_valor2)


valor1 = num1*und_valor1
valor2 = num2*und_valor2

valor_final = valor1+valor2


print("VALOR A PAGAR: {}{:.2f}".format("R$ ",valor_final))









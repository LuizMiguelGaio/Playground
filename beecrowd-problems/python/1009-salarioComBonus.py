nome = str(input())
salario = float(input())
vendas = float(input())

comissao = vendas*0.15
salario_plus = salario+comissao
salario_format = "%.2f" % salario_plus

print("TOTAL = R$", salario_format)




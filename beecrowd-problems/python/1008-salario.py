NUMBER = int(input())
hora_trab = float(input())
valor_hora = float(input())

salario = hora_trab*valor_hora
salario_format = "%.2f" % salario

print("NUMBER =", NUMBER)
print("SALARY = U$",salario_format)

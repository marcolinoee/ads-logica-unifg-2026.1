salario =float(input("Digite seu salario:"))

if (salario <=1500):
    aumento = 0.15
elif (salario > 1500 and salario <= 3000):
    aumento = 0.10
else:
    aumento = 0.05

valor_aumento = salario * aumento
valor_novo = salario + valor_aumento

print(f"Seu aumento foi de R$ {valor_aumento}")
print(f"Seu novo salário é R$ {valor_novo}")



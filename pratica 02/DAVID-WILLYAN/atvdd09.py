salario = float(input("Digite o salário: R$ "))

if salario <= 1500:
    reajuste = salario * 0.15
elif salario <= 3000:
    reajuste = salario * 0.10
else:
    reajuste = salario * 0.05

novo_salario = salario + reajuste

print(f"Salário antigo: R$ {salario:.2f}")
print(f"Reajuste: R$ {reajuste:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
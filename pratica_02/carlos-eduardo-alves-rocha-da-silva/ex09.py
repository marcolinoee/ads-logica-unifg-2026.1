# ex09.py
salario = float(input("Digite o salario: R$ "))
if salario <= 1500:
    percentual = 15
elif salario <= 3000:
    percentual = 10
else:
    percentual = 5
reajuste = salario * (percentual / 100)
novo_salario = salario + reajuste
print(f"Salario original: R$ {salario:.2f}")
print(f"Percentual: {percentual}%")
print(f"Novo salario: R$ {novo_salario:.2f}")

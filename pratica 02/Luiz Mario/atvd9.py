salario = float(input("Digite o salário atual: R$ "))

if salario <= 1500:
    percentual = 15
elif salario <= 3000:
    percentual = 10
else:
    percentual = 5

reajuste = salario * (percentual / 100)
novo_salario = salario + reajuste

print(f"\nSalário atual:    R$ {salario:.2f}")
print(f"Percentual:       {percentual}%")
print(f"Reajuste:         R$ {reajuste:.2f}")
print(f"Novo salário:     R$ {novo_salario:.2f}")
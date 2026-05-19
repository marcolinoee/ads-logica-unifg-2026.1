salario = float(input('Digite o salário: R$ '))

if salario <= 1500:
    percentual = 15
elif salario <= 3000:
    percentual = 10
else:
    percentual = 5

reajuste = salario * percentual / 100
novo_salario = salario + reajuste
print(f'Salário original: R$ {salario:.2f}')
print(f'Percentual aplicado: {percentual}%')
print(f'Novo salário: R$ {novo_salario:.2f}')
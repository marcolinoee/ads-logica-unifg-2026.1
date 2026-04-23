salario = float(input("Digite o salário do funcionário: "))
if salario <= 1500:
    aumento = salario * 0.15
elif salario >= 1500.01 and salario <= 3000:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05
    
novo_salario = salario + aumento
print(f"O novo salário do funcionário é: R${novo_salario:.2f}")
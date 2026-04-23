salario = (float(input("Digite o seu salario: ")))
if salario > 3000:
    ajuste = salario * 0.05
elif salario <= 1500:
    ajuste = salario * 0.15
else: 
    ajuste = salario * 0.10

print(f"o seu novo salario é {salario + ajuste} e seu aumento foi de {ajuste} reais")

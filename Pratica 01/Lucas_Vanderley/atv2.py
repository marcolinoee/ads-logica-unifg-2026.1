hora = int(input("Digite suas horas trabalhadas (mensais): "))
valor_h = float(input("Digite seu valor por hora: "))

salario_b = hora * valor_h
impostos = salario_b * 0.15
salario = salario_b - impostos

if hora < 1 or hora > 220:
    print("Error!")
elif valor_h < 7.37 or valor_h > 454:
    print("Os valores tem que ficar entre 7,37 e 454,00 R$!")
else:
    print("=" * 10)
    print(f"Seu Salario Bruto: {salario_b}")
    print(f"O imposto cobrado: {impostos}")
    print(f"Seu salario: {salario}")
    print("=" * 10)
valor_hora = float(input("Valor por hora: R$ "))
horas = float(input("Estimativa de horas: "))
valor_bruto = horas * valor_hora
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos
print(f"Valor bruto: R$ {valor_bruto:.2f}")
print(f"Impostos (15%): R$ {impostos:.2f}")
print(f"Valor liquido: R$ {valor_liquido:.2f}")

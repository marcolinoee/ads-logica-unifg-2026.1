valor_hora = float(input("Valor por hora trabalhadora: "))
hora_trabalhada = float(input("estimativas de horas totais trabalhadas: "))

valor_bruto = hora_trabalhada * valor_hora

impostos = valor_bruto * 0.15

valor_liquido = valor_bruto - impostos

print(f"Valor Bruto: {valor_bruto}")
print(f"Valor dos impostos: {impostos}")
print(f"Valor liquido: {valor_liquido}")
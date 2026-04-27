valor_cobrado_por_hora = float(input("Qual o valor por hora? R$"))
estimativa_horas = float(input("Quantas horas aproximadamente para concluir o projeto? "))

valor_bruto = estimativa_horas * valor_cobrado_por_hora
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print(f"O valor total bruto é: R${valor_bruto}")
print(f"O valor dos impostos sao: R${impostos}")
print(f"O valor liquido final é: R${valor_liquido}")
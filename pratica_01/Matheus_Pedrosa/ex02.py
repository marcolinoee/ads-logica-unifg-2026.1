valor_hora = float(input('Digite o valor cobrado por hora: '))
horas = float(input('Digite a estimativa de horas para conclusão: '))

valor_bruto = horas * valor_hora
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print(f'Valor bruto: R$ {valor_bruto:.2f}')
print(f'Impostos (15%): R$ {impostos:.2f}')
print(f'Valor líquido final: R$ {valor_liquido:.2f}')
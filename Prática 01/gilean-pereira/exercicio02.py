valor_hora = float(input("valor da hora:"))
estimativa = int(input("digite sua estimativa em h:"))

valor_bruto = estimativa * valor_hora
imposto = valor_bruto * 0.15
valor_liquido = valor_bruto - imposto

print("valor bruto:",valor_bruto)
print("imposto:",imposto)
print("valor liquido",valor_liquido)
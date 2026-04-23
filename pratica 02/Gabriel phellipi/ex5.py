contar_positivos = 0
for i in range (1,11):
    numero = (float(input(f"Digite o {i}º numero: ")))
    if numero > 0:
        contar_positivos += 1
print(f"a quantidade de numero positivos é {contar_positivos}")        
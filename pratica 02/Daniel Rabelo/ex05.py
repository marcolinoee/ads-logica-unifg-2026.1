contador_positivos = 0
numeros_positivos = []

for i in range(1,11):
    numero = float(input(f"Digite o {i}° número: "))
    if numero > 0:
        contador_positivos += 1
        numeros_positivos.append(numero)
print("---")
print(f"Total de números positivos: {contador_positivos}")

if numeros_positivos:
    print(f"Os números positivos digitados foram: {numeros_positivos}")
else:
    print("Nenhum número positivo foi digitado.")


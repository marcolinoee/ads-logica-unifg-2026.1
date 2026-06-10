# ex05.py
contador_positivos = 0
for i in range(1, 11):
    numero = float(input(f"Digite o {i} numero: "))
    if numero > 0:
        contador_positivos += 1
print(f"Quantidade de numeros positivos: {contador_positivos}")

# ex07.py
soma_pares = 0
for i in range(1, 9):
    numero = int(input(f"Digite o {i} numero: "))
    if numero % 2 == 0:
        soma_pares += numero
print(f"Soma dos numeros pares: {soma_pares}")

oma_pares = 0

for i in range(8):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero % 2 == 0:
        soma_pares += numero

print("Soma dos números pares:", soma_pares)
numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior_valor = numeros[0][0]
menor_valor = numeros[0][0]

for linha in numeros:

    for numero in linha:
        if numero > maior_valor:
            maior_valor = numero
            
        if numero < menor_valor:
            menor_valor = numero

print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
numeros = [[12,5,8],[9,21,3],[14,6,18]]
maior = numeros[0][0]
menor = numeros[0][0]
for linha in numeros:
    for v in linha:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
print("Maior valor:", maior)
print("Menor valor:", menor)

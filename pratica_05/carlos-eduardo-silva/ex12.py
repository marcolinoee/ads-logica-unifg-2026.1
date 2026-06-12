numeros = [[12,5,8],[9,21,3],[14,6,18]]
maior = numeros[0][0]
li, co = 0, 0
for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        if numeros[i][j] > maior:
            maior = numeros[i][j]
            li, co = i, j
print("Maior valor:", maior)
print("Linha:", li)
print("Coluna:", co)

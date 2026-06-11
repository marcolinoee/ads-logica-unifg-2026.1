valores = [[3,5,7],[2,4,6],[1,8,9]]
pares = 0
for linha in valores:
    for v in linha:
        if v % 2 == 0:
            pares += 1
print("Quantidade de pares:", pares)

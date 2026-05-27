valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

soma = 0
for linha in valores:
    for v in linha:
        soma += v

print("Soma total:", soma)

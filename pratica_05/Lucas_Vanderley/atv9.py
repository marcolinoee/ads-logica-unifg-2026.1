valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

soma_total = 0

for linha in valores:

    for numero in linha:
        soma_total = soma_total + numero # ou soma_total += numero

print(f"Soma total: {soma_total}")
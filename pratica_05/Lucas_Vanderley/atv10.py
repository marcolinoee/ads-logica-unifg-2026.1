valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

qtd_pares = 0

for linha in valores:
    for numero in linha:
        if numero % 2 == 0:
            qtd_pares = qtd_pares + 1  # ou qtd_pares += 1

print(f"Quantidade de pares: {qtd_pares}")
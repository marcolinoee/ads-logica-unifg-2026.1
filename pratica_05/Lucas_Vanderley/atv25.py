tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

linha, coluna = 1, 0


if tabuleiro[linha][coluna] == " ":
    tabuleiro[linha][coluna] = "X"
    print("Jogada realizada com sucesso!\n")
else:
    print("Jogada inválida! Posição já ocupada.\n")


print("Tabuleiro atualizado:")
for i, l in enumerate(tabuleiro):
    print(" | ".join(l))
    if i < 2:
        print("-" * 9)
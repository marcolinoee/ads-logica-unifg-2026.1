tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

linha = 1
coluna = 0
simbolo = "X"

if tabuleiro[linha][coluna] == " ":
    tabuleiro[linha][coluna] = simbolo
    print("Jogada realizada.")
else:
    print("Jogada inválida.")

for i in range(len(tabuleiro)):
    print(" | ".join(tabuleiro[i]))
    if i < len(tabuleiro) - 1:
        print("---------")

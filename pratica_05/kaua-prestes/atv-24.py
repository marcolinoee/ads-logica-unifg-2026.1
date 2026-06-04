tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

for i in range(len(tabuleiro)):
    print(" | ".join(tabuleiro[i]))
    if i < len(tabuleiro) - 1:
        print("---------")

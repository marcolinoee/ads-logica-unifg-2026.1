tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

for i, linha in enumerate(tabuleiro):
    print(" | ".join(linha))
    
    if i < 2:
        print("-" * 9)
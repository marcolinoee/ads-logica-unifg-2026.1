tabuleiro = [["X","O"," "],[" ","X","O"],["O"," ","X"]]
if tabuleiro[1][0] == " ":
    tabuleiro[1][0] = "X"
    print("Jogada realizada!")
else:
    print("Jogada inválida!")
for i in range(len(tabuleiro)):
    print(" | ".join(tabuleiro[i]))
    if i < 2:
        print("---------")

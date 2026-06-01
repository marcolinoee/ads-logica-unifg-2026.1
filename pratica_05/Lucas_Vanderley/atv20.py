sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

linha, coluna = 2, 1

if sala[linha][coluna] == "L":
    sala[linha][coluna] = "O"
    print("Reserva realizada.\n")
else:
    print("Assento indisponível.\n")

print("Matriz atualizada:")
for linha_sala in sala:
    print(linha_sala)
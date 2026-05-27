sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

linha = 2
coluna = 1

if sala[linha][coluna] == "L":
    sala[linha][coluna] = "O"
    print("Reserva realizada.")
else:
    print("Assento indisponível.")

for l in sala:
    print(l)

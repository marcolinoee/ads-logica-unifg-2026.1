sala = [["L","O","L"],["O","O","L"],["L","L","O"]]
if sala[2][1] == "L":
    sala[2][1] = "O"
    print("Reserva realizada")
else:
    print("Assento indisponível")
for linha in sala:
    print(linha)

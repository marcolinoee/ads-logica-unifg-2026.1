sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

todos_assentos = [assento for linha in sala for assento in linha]

livres = todos_assentos.count("L")
ocupados = todos_assentos.count("O")

print(f"Assentos livres: {livres}\nAssentos ocupados: {ocupados}")
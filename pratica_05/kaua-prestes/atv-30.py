laboratorio = [
    ["L", "O", "L", "M", "L"],
    ["O", "L", "L", "O", "M"],
    ["L", "L", "O", "L", "L"],
    ["M", "O", "L", "L", "O"]
]

print("Mapa do laboratório:")
for linha in laboratorio:
    print(linha)

livres = ocupados = manutencao = 0
for linha in laboratorio:
    for comp in linha:
        if comp == "L":
            livres += 1
        elif comp == "O":
            ocupados += 1
        elif comp == "M":
            manutencao += 1

print(f"\nLivres: {livres} | Ocupados: {ocupados} | Manutenção: {manutencao}")

fileira = int(input("\nFileira para ocupar (0-3): "))
computador = int(input("Computador para ocupar (0-4): "))

if fileira < 0 or fileira >= len(laboratorio) or computador < 0 or computador >= len(laboratorio[0]):
    print("Posição fora dos limites da matriz.")
elif laboratorio[fileira][computador] == "M":
    print("Computador em manutenção. Operação não permitida.")
elif laboratorio[fileira][computador] == "O":
    print("Computador já está ocupado.")
else:
    laboratorio[fileira][computador] = "O"
    print("Computador ocupado com sucesso.")
    print("\nMapa atualizado:")
    for linha in laboratorio:
        print(linha)

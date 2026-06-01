lab = [
    ["L", "O", "M", "L", "L"],
    ["O", "O", "L", "L", "M"],
    ["L", "M", "O", "O", "L"],
    ["L", "L", "L", "M", "O"]
]


print("--- MAPA DO LABORATÓRIO ---")
for i, fileira in enumerate(lab):
    print(f"Fileira {i}: {' '.join(fileira)}")
print("-" * 27)


todos_pcs = [pc for fileira in lab for pc in fileira]
print(f"Livres (L): {todos_pcs.count('L')}")
print(f"Ocupados (O): {todos_pcs.count('O')}")
print(f"Manutenção (M): {todos_pcs.count('M')}\n")


try:
    linha_digitada = int(input("Digite a fileira (0 a 3): "))
    coluna_digitada = int(input("Digite o computador (0 a 4): "))
    

    if not (0 <= linha_digitada < 4 and 0 <= coluna_digitada < 5):
        print("Erro: Posição digitada está fora dos limites da matriz.")
    else:
        estado_atual = lab[linha_digitada][coluna_digitada]
        
        if estado_atual == "M":
            print("Ação negada: Computador em manutenção.")
        elif estado_atual == "O":
            print("Ação negada: Computador já ocupado.")
        else:
            lab[linha_digitada][coluna_digitada] = "O"
            print("Sucesso: Computador ocupado com sucesso!")
            
except ValueError:
    print("Erro: Por favor, digite apenas números inteiros válidos.")
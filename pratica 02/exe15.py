maior = float(input("Digite a 1ª nota: "))

for i in range(4):
    nota = float(input(f"Digite a {i+2}ª nota: "))
    
    if nota > maior:
        maior = nota

print(f"Maior nota: {maior}")
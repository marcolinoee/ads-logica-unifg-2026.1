maior = -1

for i in range(1, 6):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    if nota > maior:
        maior = nota

print(f"\nA maior nota foi: {maior:.1f}")
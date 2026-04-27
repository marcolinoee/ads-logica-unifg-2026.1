maior_nota = 0

print("Digite as 5 notas dos alunos:")

for i in range(1, 6):
    nota = float(input(f"Digite a {i}° nota: "))
    if nota > maior_nota:
        maior_nota = nota

print("-" * 30)        
print(f"A maior nota encontrada no grupo foi: {maior_nota}")
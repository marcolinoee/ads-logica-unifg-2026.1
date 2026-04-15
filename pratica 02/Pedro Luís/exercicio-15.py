import os 
os.system("cls" if os.name == "nt" else "clear")

maior = 0
for i in range(0, 5):
    while True:
        try:    
            nota = float(input(f"Digite a nota do {i + 1}° aluno: "))
        except ValueError:
            print("DIGITE APENAS NÚMEROS REAIS NESSA OPÇÃO!")
            continue
        break
    if i == 0:
        maior = nota
    else:
        if nota > maior:
            maior = nota
print("-" * 45)
print(f"A maior nota entre os cinco alunos foi {maior}")

import os 
os.system("cls" if os.name == "nt" else "clear")

while True:
    try:    
        alunos = int(input("Digite quantos alunos a sua escola tem: "))
    except ValueError:
        print("DIGITE APENAS NÚMEROS INTEIROS NESSA OPÇÃO!")
        continue
    break
reprovado = 0
aprovado = 0
recuperação = 0
for i in range(0, alunos):
    while True:
        try:
            media = float(input(f"Digite a media do {i + 1}° aluno: "))
        except ValueError:
            print("DIGITE APENAS NÚMEROS INTEIROS NESSA OPÇÃO!")
            continue
        break
    if media < 4:
        reprovado += 1
    elif 4 <= media < 7:
        recuperação += 1
    else:
        aprovado += 1
print("-" * 35)
print(f"Foram aprovados {aprovado} alunos.\n{recuperação} alunos ficaram de recuperação.\nForam reprovrados {reprovado} alunos.")
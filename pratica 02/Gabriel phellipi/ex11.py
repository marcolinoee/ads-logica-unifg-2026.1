quantidade = (int(input("Digite a quantidade de alunos:")))
aprovados = 0
reprovados = 0
recuperacao = 0
for i in range (0, quantidade):
    medias = (float(input("Digite a media desse aluno: ")))
    if medias >= 7 and medias <= 10:
        aprovados += 1
    elif medias >= 4 and medias < 6.9:
        recuperacao += 1
    elif medias < 4 and medias > 0:
        reprovados += 1
    else:
        print("digite uma nota valida")    
        break

print(f"{aprovados} alunos foram aprovados")
print(f"{recuperacao} alunos ficaram de recuperação")
print(f"{reprovados} alunos foram reprovados")
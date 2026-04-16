quantidade=int(input("quantidade de alunos:"))
aprovados=0
recuparacao=0
reprovados=0
for i in range (quantidade):
  media=float(input("digite a media do aluno:"))
  if media >=7:
    aprovados+=1
  elif media>=5:
    recuperacao+=1
  else:
    reprovados+=1
    print("aprovados:",aprovados)
    print("recuperacao:",recuperacao)
    print("reprovados:",reprovados)

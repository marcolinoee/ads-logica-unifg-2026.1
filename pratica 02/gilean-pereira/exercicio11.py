alunos = 0
passou = 0
nao_passou = 0
recuperacao = 0

while (alunos < 5):
  nota_1 = float(input("digite sua nota 1:"))
  nota_2 = float(input("digite sua nota 2:"))
  nota_3 = float(input("digite sua nota 3:"))
  media = (nota_1+nota_2+nota_3)/3
  print(media)
  if(media >=7):
      passou+=1
  elif(media >=4):
    recuperacao+=1
  else:
    nao_passou+=1
  alunos+=1
print(f"{alunos} Alunos")
print(f"{passou} Alunos aprovados")
print(f"{recuperacao} Alunos de recuperação")
print(f"{nao_passou} Alunos reprovados")
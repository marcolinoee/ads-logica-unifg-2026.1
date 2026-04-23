Students = int(input("Digite a quantidade de alunos : "))
Students_approved = 0
Students_Catching_up = 0
Students_failed = 0

for School in range (Students):
    average = int(input("Digite sua media : "))
    if average>=7:
        Students_approved+=1
    elif average>=4:
        Students_Catching_up+=1
    else:
        Students_failed+=1
print(f"Estudantes aprovados {Students_approved} , Estudantes de recuperação {Students_Catching_up} e reprovados {Students_failed} ")
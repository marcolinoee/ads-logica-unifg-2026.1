import random

for a in range(26):
    media = random.randint(0, 10)
    print(f"O aluno {a} deve determinada media de: {media}")

    if media >= 7:
      print("Aprovado\n")
    elif media <= 6:
      print("Recuperação\n")
    elif  media < 4:
      print("Reprovado\n")

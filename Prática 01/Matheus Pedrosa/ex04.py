idade = int(input("Digite a sua idade: "))
anosExperiencia = int(input("Quantos anos de experiência você possui? "))

acesso = (idade >= 18) and (anosExperiencia > 2)

print(f"\033[1;33mAcesso liberado:   {acesso}\033[m")
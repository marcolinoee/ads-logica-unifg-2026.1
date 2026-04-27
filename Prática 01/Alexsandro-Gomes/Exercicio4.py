IdadeDoUsuario = int(input("Qual a sua idade : "))
Experiencia = int(input("Quantos anos de experiencia no trabalho : "))
Acesso = (IdadeDoUsuario>=18) and (Experiencia>2)

print(Acesso)
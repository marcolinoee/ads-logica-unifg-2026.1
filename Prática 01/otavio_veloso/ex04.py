idade_usuario = int(input("Qual a sua idade? "))
anos_de_profissao = int(input("Quantos anos você tem de experiência? "))

acesso = (idade_usuario >= 18) and (anos_de_profissao > 2)

print(f"Acesso liberado: {acesso}")
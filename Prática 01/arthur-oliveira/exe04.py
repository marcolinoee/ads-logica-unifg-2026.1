idade = int(input("Digite sua idade: "))
experiencia = int(input("Digite seus anos de experiência: "))

acesso = (idade >= 18) and (experiencia > 2)

print(f"Acesso Liberado: {acesso}")
idade = int(input("Digite a sua idade: "))
experiencia = int(input("Anos de experiencia: "))
acesso = (idade >= 18) and (experiencia > 2)
print(f"Acesso Liberado: {acesso}")

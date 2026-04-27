nome_usuario = input("Qual o seu nome? ")
ano_nascimento = int(input("Em que ano você nasceu? "))
altura = float(input("Qual sua altura(metros)? "))
ano_atual = 2026

idade = ano_atual - ano_nascimento

print(f"Olá, {nome_usuario}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.")
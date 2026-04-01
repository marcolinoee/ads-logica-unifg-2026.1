nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
altura = float(input("Digite sua altura: "))
ano_atual = 2026

idade = ano_atual - ano_nascimento

print(f"Olá {nome}! Você tem {idade} e sua altura é de {altura}m. Registro concluído")
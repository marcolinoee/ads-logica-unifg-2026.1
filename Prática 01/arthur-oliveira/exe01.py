nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite o ano que você nasceu: "))
altura = float(input("Digite sua altura em metros: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual- ano_nascimento 

print(f"Olá {nome}! Você tem {idade} e a sua altura é {altura}m. Registro concluído")
nomeUsuario = str(input("Digite o seu nome: ")).strip()
dataNascimento = int(input("Em que ano você nasceu?: "))
altura = float(input("Qual é a sua altura: "))
anoAtual = 2026

idade = anoAtual - dataNascimento

print(f"Olá, {nomeUsuario}! Você tem {idade} e sua altura é {altura}m. Registro concluido.")
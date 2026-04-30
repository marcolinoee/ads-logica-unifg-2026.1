nome = str(input("Digite seu nome: "))
nascimento = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura: "))

idade = 2026 - nascimento


if nascimento >= 2026 or idade > 100 or altura > 2.72:
    print("Error!")
else:
    print("=" * 10)
    print(f"Olá,{nome}! Você tem {idade} anos e sua altura é de {altura}m.\nRegistro concluído...")
    print("=" * 10)
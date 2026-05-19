nome = input('Digite o nome do usuário: ').strip()
ano_nascimento = int(input('Digite o ano de nascimento: '))
altura = float(input('Digite a altura em metros: '))

ano_atual = 2026
idade = ano_atual - ano_nascimento

print(f'Olá, {nome}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.')
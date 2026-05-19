idade = int(input('Digite a idade: '))
experiencia = int(input('Digite os anos de experiência: '))

acesso = (idade >= 18) and (experiencia > 2)
print(f'Acesso Liberado: {acesso}')



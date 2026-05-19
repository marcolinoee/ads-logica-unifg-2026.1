idade = int(input('Digite a idade: '))

if idade < 18:
    print('Menor de idade.')
elif idade < 60:
    print('Maior de idade.')
else:
    print('Idosa.')

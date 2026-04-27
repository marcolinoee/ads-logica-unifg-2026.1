idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de Idade")
elif idade <= 59:
    print("Maior de idade")
elif idade > 59:
    print("Idoso")
else:
    print("Error!")
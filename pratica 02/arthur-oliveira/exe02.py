idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade")
elif idade <= 59:
    print("Maior de idade")
else:
    print("Idoso")
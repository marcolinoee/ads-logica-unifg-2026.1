idade = int(input("Digite a idade: "))

if idade <= 17:
    print("A pessoa é menor de idade.")
elif idade <= 59:
    print("A pessoa é adulta.")
elif idade >= 60:
    print("A pessoa é idosa.")
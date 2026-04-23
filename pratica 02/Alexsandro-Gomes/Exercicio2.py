Idade = int(input("Qual sua idade : "))
if (Idade<18) :
    print("Menor de idade : Menos de 18 anos")
elif (Idade>=18) and (Idade<=59):
    print("Maior de idade : Entre 18 a 59 anos")
else :
    print("Idoso : 60 anos ou mais")
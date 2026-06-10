# ex06.py
nota = float(input("Digite uma nota de 0 a 10: "))
while nota < 0 or nota > 10:
    print("Nota invalida!")
    nota = float(input("Digite uma nota de 0 a 10: "))
print(f"Nota aceita: {nota}")

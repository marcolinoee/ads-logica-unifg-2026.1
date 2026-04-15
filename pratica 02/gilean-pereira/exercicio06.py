nota = float(input("Digite uma nota de 0 a 10:"))

while(nota < 0 or nota > 10):
    nota = float(input("Nota invalida! Digite novamente uma nota de 0 a 10:"))
print(f"Sua nota:{nota}")
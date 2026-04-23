nota = int(input("Digite sua nota de 0 a 10 : "))
while (nota<0) or (nota>10):
    nota = int(input("Nota invalida tente novamente : "))
print(f"Sua nota e {nota}")
    
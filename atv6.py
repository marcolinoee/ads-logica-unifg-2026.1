while True:
    nota = int(input("Digite uma nota de 0 a 10: "))

    if nota > 10:
        print("Maior que 10")
    elif nota < 0:
        print("Menor que 0")
    else: 
        print("Ok!")
    break

   
print("Fim do Programa!")
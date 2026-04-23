nota = (float(input("Digite a nota: ")))
while nota < 0 or nota > 10:
    nota = (float(input("digite uma nota válida(entre 0 e 10): ")))
    if nota > 0 and nota <= 10:
        print("Nota válida!")
        break
    

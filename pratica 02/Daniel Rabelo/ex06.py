nota = -1

while nota < 0 or nota > 10:
    nota = float(input("Digite uma nota entre 0 e 10: "))

    if nota < 0 or nota > 10:
        print("Valor inválido! A nota deve estar no intervalo de 0 a 10.")

print(f"Sucesso! Você digitou a nota: {nota}")
import os 
os.system("cls" if os.name == "nt" else "clear")

soma = 0
pares = []
for i in range(0, 8):
    while True:
        try:
            numeros = int(input("Digite um número inteiro: "))
        except ValueError:
            print("DIGITE APENAS NÚMEROS INTEIROS!")
            continue
        break
    if numeros % 2 == 0:
        pares.append(numeros)
        soma += numeros
print(f"Os números pares foram {pares}, e a soma deles dá {soma}")
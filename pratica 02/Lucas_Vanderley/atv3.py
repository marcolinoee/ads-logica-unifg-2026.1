numero = int(input("Digite seu valor: "))

if numero % 2 == 0:
    for numero in range(0, numero + 1):
        print(f"Contando: {numero}")
else:
    print("Error!")
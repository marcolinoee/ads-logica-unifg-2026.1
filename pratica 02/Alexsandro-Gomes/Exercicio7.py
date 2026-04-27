contador = 0 
for numero in range (1,9):
    numericao = int(input("Digite o numero : "))
    if (numericao % 2 == 0):
        contador = contador + numericao
print(f"Esses numeros possui {contador} somas de pares")
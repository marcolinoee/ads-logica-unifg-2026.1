contador_numero = 0

for numeros in range(1,11):
    numeros = int(input("Digite um numero:"))
    if(numeros >= 0):
        contador_numero +=1

print(f"{contador_numero} numeros positivos")
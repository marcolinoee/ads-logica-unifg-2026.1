positivo = 0

for i in range(10):
    num= float(input("digite seus números:"))

    if num >= 0:
        positivo = positivo + 1 

print("a quantidade de numeros positivos é de ", positivo)
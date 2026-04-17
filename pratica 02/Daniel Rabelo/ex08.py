numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
print("-" * 15)

for i in range(1,10):
    resultado = numero * i 
    print(f"{numero} x {i} = {resultado}")

print("-" * 15)
soma_pares = 0

print("Por favor, digite 8 números inteiros:")
for i in range(1,9):
    numero = int(input(f"Digite o {i}° valor: "))
    if numero % 2 == 0:
        soma_pares = soma_pares + numero
        print(f"-> {numero} é par e foi adicionado à soma.")
    else: 
        print(f"->{numero} é ímpar e foi ignorado")

print("---")
print(f"A soma total dos números pares digitados é: {soma_pares}")
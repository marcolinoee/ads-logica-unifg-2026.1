while True:
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("DIGITE APENAS NÚMEROS INTEIROS!")
        continue
    break
if numero > 0:
    print(f"O número {numero} é POSITIVO!")
elif numero < 0:
    print(f"O número {numero} é NEGATIVO!")
else:
    print("O número é ZERO.")

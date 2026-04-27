import os 
os.system("cls" if os.name == "nt" else "clear")

while True:
    try:
        numero = int(input("Digite um número para mostrar a sua tabuada: "))
    except ValueError:
        print("DIGITE APENAS NÚMEROS INTEIROS!")
        continue
    break
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

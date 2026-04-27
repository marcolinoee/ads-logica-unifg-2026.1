import os 
os.system("cls" if os.name == "nt" else "clear")
p = []
positivos = 0
for i in range(0, 10):
    while True:
        try:
            numeros = int(input("Digite um número: "))
        except ValueError:
            print("DIGITE APENAS NÚMEROS INTEIROS!")
            continue
        break
    if numeros > 0:
        p.append(numeros)
        positivos += 1
print(f"{positivos} números inscritos foram positivos.\nforam eles {p if len(p) > 0 else "nenhum."}")

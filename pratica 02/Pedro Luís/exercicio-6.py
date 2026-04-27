import os 
os.system("cls" if os.name == "nt" else "clear")

while True:
    try:
        entrada = input("Digite a sua nota: ").strip().replace(",", ".")
        nota = float(entrada)
        if nota > 10  or nota < 0:
            print("Apenas notas entre 0 a 10 podem ser aceitas")
            continue
    except ValueError:
        print("DIGITE APENAS NÚMEROS REAIS")
        continue
    break
if nota < 5:
    print("Ei pô, bora melhorar um pouquinho essa nota aí.")
elif 5 <= nota < 7:
    print("Tá boa, mas dá pra melhorar.")
else:
    print("Oxe, passou o carro mano.")
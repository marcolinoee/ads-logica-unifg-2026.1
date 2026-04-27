valor = float(input("Digite seu valor: "))


if valor < 1500:
    bonus = valor * 0.15 
elif valor < 3000:
    bonus = valor * 0.10 
else: 
    bonus = valor * 0.05

resultado = valor + bonus
print(f"Seu acrescimo é de {bonus:.2f} // {valor} + {bonus:.2f} = {resultado}")
print("Fim do programa!")


fatiasPizza = int(input("Quantas fatias de pizza tem? "))
programadores = int(input("Quantos programadores? "))

pizzaPessoa = fatiasPizza // programadores
sobrasPizza = fatiasPizza % programadores

print(f"A divisão vai ficar {pizzaPessoa} pizzas para cada.")
print(f"Vai sobrar {sobrasPizza} pizzas.")
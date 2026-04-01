numero_pizza = int(input("Numero total de fatias: "))
numero_programador = int(input("Numero de programadores: "))

fatias_pessoa = numero_pizza // numero_programador

sobra = numero_pizza % numero_programador

print(f"Fatias para cada programador: {fatias_pessoa}")
print(f"Sobraram {sobra} fatias: ")
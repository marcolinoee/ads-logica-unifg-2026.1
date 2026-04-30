fatias = int(input("Digite quantas fatias a pizza tem: "))
programadores = int(input("Quantos programadores tem: "))


if fatias < 1 or fatias > 9 or programadores < 1 or programadores > 9:
    print("Error!")
else:
 fatiasp = fatias // programadores
 sobra = fatias % programadores

print("=" * 10)
print (f"Cada programador comeu {fatiasp} fatias.")
print(f"Sobrou {sobra} fatias.")
print("=" * 10)
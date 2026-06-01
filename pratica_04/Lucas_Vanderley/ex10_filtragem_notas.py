notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]

notas.clear()
notas.append(7.0)
notas.append(8.0)
notas.append(9.5)

print(notas)

print("=" * 30)

for i in range(len(notas)):
    if notas[i] >= 7.0:
        print(f"A nota {notas[i]} foi aprovada!")

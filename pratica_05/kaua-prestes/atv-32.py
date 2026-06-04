grade = [
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0]
]

print("Grade inicial:")
for linha in grade:
    print(linha)

ocupadas = 0
for linha in grade:
    for cel in linha:
        if cel == 1:
            ocupadas += 1
print("Células ocupadas:", ocupadas)

grade[0][2] = 1
grade[1][1] = 1
grade[3][4] = 1

print("\nGrade após alterações:")
for linha in grade:
    print(linha)

ocupadas = 0
for linha in grade:
    for cel in linha:
        if cel == 1:
            ocupadas += 1
print("Células ocupadas:", ocupadas)

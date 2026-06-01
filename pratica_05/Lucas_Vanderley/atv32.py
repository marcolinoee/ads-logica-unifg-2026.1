grade = [[0] * 5 for _ in range(5)]

def exibir_grade(g):
    for linha in g:
        print(" ".join(map(str, linha)))


print("--- GRADE INICIAL ---")
exibir_grade(grade)

print(f"Células ocupadas: {sum(celula for linha in grade for celula in linha)}\n")


grade[0][0] = 1
grade[2][3] = 1
grade[4][1] = 1


print("--- GRADE DEPOIS DA SIMULAÇÃO ---")
exibir_grade(grade)
print(f"Células ocupadas: {sum(celula for linha in grade for celula in linha)}")
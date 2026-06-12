grade = [[0,1,0,0,1],[1,0,0,1,0],[0,0,1,0,0],[1,0,0,0,1],[0,1,0,1,0]]
print("Antes:")
for linha in grade:
    print(linha)
print("Ocupadas antes:", sum(l.count(1) for l in grade))
grade[0][0] = 1
grade[1][2] = 1
grade[3][2] = 1
print("Ocupadas depois:", sum(l.count(1) for l in grade))
print("Depois:")
for linha in grade:
    print(linha)

nota = float(input('Digite uma nota de 0 a 10: '))
while nota < 0 or nota > 10:
    nota = float(input('Entrada inválida. Digite uma nota de 0 a 10: '))
print(f'Nota válida: {nota:.1f}')
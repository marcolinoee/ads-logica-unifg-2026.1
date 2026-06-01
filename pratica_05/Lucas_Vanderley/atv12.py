numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]


maior_valor = numeros[0][0]
linha_maior = coluna_maior = 0

for i, linha in enumerate(numeros):
    for j, valor in enumerate(linha):
        if valor > maior_valor:
            maior_valor = valor
            linha_maior, coluna_maior = i, j 

print(f"Maior valor: {maior_valor}\nLinha: {linha_maior}\nColuna: {coluna_maior}")
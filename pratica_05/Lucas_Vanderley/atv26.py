dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

for linha in dados:
    for valor in linha:
        print(valor)

'''
Qual erro pode ocorrer?
O código vai gerar um erro do tipo IndexError: list index out of range

Por que esse erro acontece?
O loop interno tenta rodar fixamente 3 vezes (j varia de 0 a 2) para todas as linhas. 
Porém, a segunda linha (dados[1]) possui apenas dois elementos ([4, 5]). 
Quando o programa tenta acessar dados[1][2], o índice não existe e o programa quebra.
'''
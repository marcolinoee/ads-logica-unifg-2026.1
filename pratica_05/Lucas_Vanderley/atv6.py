dados = [
    [1, 2],
    [3, 4]
]

# Acessa a segunda linha [1] e a primeira coluna [0]
print(dados[1][0])  # Retorna: 3

#Esse código executa corretamente? Por quê? 
"Não. Ele vai gerar um erro do tipo IndexError: list index out of range (Índice fora do intervalo). "
"Isso acontece porque o código tenta acessar a linha de índice 2 (que seria uma terceira linha), "
"mas a matriz dados possui apenas duas linhas (índices 0 e 1)."
#Quais são os índices válidos para as linhas dessa matriz?
"Os únicos índices de linha válidos são 0 (para a primeira linha [1, 2]) "
"e 1 (para a segunda linha [3, 4])."
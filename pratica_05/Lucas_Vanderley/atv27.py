# Cria listas independentes na memória
matriz = [[0] * 3 for _ in range(3)]
matriz[0][0] = 1

print(matriz)  # Retorna: [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

'''
Qual resultado provavelmente será exibido?
O resultado será: [[1, 0, 0], [1, 0, 0], [1, 0, 0]].

Por que esse comportamento pode confundir iniciantes?
Porque o comando altera apenas a posição [0][0], mas o número 1 aparece em todas as linhas. 
Isso confunde porque o operador * 3 não cria cópias independentes das linhas, ele cria ref
erências para a mesma lista na memória. 
Alterar uma linha altera todas as outras ao mesmo tempo.
'''
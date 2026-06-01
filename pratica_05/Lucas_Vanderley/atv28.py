notas = [
    [8, 7, 9],
    [5, 6, 5],
    [9, 10, 8]
]

for linha in notas:
    # A função sum() calcula a soma isolada desta linha atual
    media = sum(linha) / len(linha)
    print(media)

'''
Qual é o problema com a variável soma?
A variável soma foi declarada fora dos loops e nunca é resetada. 
Assim, a nota dos alunos anteriores acumula no cálculo do próximo aluno, 
gerando médias absurdamente altas e erradas.

Por que a correção funciona?
Ao eliminar a variável global acumuladora e usar sum(linha), o Python calcula a soma estritamente 
para a sublista daquela iteração. Cada aluno tem suas notas somadas do zero, sem herdar o lixo de 
memória do estudante anterior.
'''
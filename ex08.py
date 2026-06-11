# Erro original: faltava ':' no final da linha 'def saudacao(nome)'
# Tipo de erro: SINTATICO (SyntaxError)
# O programa nao executava porque o Python nao conseguia
# interpretar a definicao da funcao sem os dois pontos.

# Codigo corrigido:
def saudacao(nome):
    print("Ola,", nome)

saudacao("Joao")

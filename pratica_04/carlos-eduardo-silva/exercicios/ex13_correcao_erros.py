# Exercício 13 - Erros comuns e correção

# Trecho A - lista.sort() retorna None, por isso não se atribui a uma variável
lista = [3, 1, 2]
lista.sort()
print(lista)

# Trecho B - índice 5 não existe numa lista de 2 elementos
nomes = ["Ana", "Bruno"]
indice = 5
if indice < len(nomes):
    print(nomes[indice])
else:
    print(f"Índice {indice} não existe na lista.")

# Desafio: strings são imutáveis, não se altera um caractere diretamente
palavra = "python"
palavra = "P" + palavra[1:]
print(palavra)

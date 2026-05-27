# a) sort() não retorna a lista, ele altera a propria lista e retorna none
lista = [3, 1, 2]
resultado = lista.sort()
print(resultado)  # imprime None

#correção:
lista = [3, 1, 2]
lista.sort()
print(lista)

# b) a lista tem apenas 2 elementos, então o indice 5 não existe

nomes = ["Ana", "Bruno"]
# print(nomes[5])  
# daria erro: IndexError

#correção:
nomes = ["Ana", "Bruno"]

if 5 < len(nomes):
    print(nomes[5])
else:
    print("Índice inválido")
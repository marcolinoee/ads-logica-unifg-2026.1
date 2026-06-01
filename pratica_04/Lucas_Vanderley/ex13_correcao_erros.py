
lista = [3, 1, 2]
lista.sort()
print(lista)

print("-" * 30)


nomes = ["Ana", "Bruno"]
indice_desejado = 5

if indice_desejado < len(nomes):
    print(nomes[indice_desejado])
else:
    print(f"Erro: O índice {indice_desejado} não existe na lista.")

print("-" * 30)


nome = "Anu"
nome_corrigido = nome.replace("u", "a")
print(nome_corrigido)
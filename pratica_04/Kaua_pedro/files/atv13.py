lista = [3, 1, 2]
lista.sort()
print("Lista ordenada:", lista)

lista2 = [3, 1, 2]
resultado = sorted(lista2)
print("Resultado com sorted():", resultado)

nomes = ["Ana", "Bruno"]
indice = 5

if indice < len(nomes):
    print("Nome:", nomes[indice])
else:
    print(f"Índice {indice} inválido. A lista tem apenas {len(nomes)} elemento(s).")

texto = "Python"
texto = texto + " é legal"
print(texto)

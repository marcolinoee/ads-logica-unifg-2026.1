# Exercício 2 - Separando e reunindo texto
nome_completo = "Maria Clara Souza"
partes = nome_completo.split()
print(partes)
nome_hifenizado = "-".join(partes)
print(nome_hifenizado)
print(f"Primeiro nome: {partes[0]}")
print(f"Último sobrenome: {partes[-1]}")

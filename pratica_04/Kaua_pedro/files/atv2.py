nome_completo = "Maria Clara Souza"

partes = nome_completo.split()
print("Lista de partes:", partes)

nome_hifenizado = "-".join(partes)
print("Nome com hífen:", nome_hifenizado)

print("Primeiro nome:", partes[0])
print("Último sobrenome:", partes[-1])

# dados iniciais
nomes_brutos = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
consulta = "joão"

# padronização dos nomes
nomes = []
for nome in nomes_brutos:
    nomes.append(nome.strip().title())

# filtragem de notas aprovadas
aprovados = []
for nota in notas:
    if nota >= 7.0:
        aprovados.append(nota)

# verificação de presença
consulta_padronizada = consulta.strip().title()
presente = False

for nome in nomes:
    if nome == consulta_padronizada:
        presente = True
        break

# relatório final
print("Lista de nomes padronizados:")
print(nomes)

print("\nNotas aprovadas:")
print(aprovados)

print("\nConsulta de presença:")
if presente:
    print(f"{consulta_padronizada} está presente")
else:
    print(f"{consulta_padronizada} não está presente")
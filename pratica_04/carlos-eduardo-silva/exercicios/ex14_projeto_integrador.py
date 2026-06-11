# Exercício 14 - Projeto integrador curto

# Etapa 1: Padronizar nomes
nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]
nomes_padronizados = []
for nome in nomes_brutos:
    nomes_padronizados.append(nome.strip().title())

# Etapa 2: Filtrar notas aprovadas
notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
aprovados = []
for nota in notas:
    if nota >= 7.0:
        aprovados.append(nota)

# Etapa 3: Verificar presença
consulta = "carla silva"
consulta_padronizada = consulta.strip().title()
encontrado = False
for nome in nomes_padronizados:
    if nome == consulta_padronizada:
        encontrado = True
        break

# Etapa 4: Relatório final
print("===== RELATÓRIO FINAL =====")
print(f"Alunos: {nomes_padronizados}")
print(f"Notas aprovadas: {aprovados}")
print(f"Total de aprovados: {len(aprovados)}")
if encontrado:
    print(f"Presença de '{consulta_padronizada}': CONFIRMADA")
else:
    print(f"Presença de '{consulta_padronizada}': NÃO ENCONTRADA")
print("===========================")

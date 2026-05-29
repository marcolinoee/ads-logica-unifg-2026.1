nomes_brutos = ["  ana souza", "BRUNO LIMA  ", "cArLa silva", "  joão pedro  ", "FERNANDA  "]
nomes_padronizados = []

for nome in nomes_brutos:
    nomes_padronizados.append(nome.strip().title())

print("=== Etapa 1: Nomes Padronizados ===")
for nome in nomes_padronizados:
    print(" -", nome)

notas = [4.5, 7.0, 8.5, 5.5, 9.0, 6.8, 7.2, 3.0, 8.0]
aprovados = []

for nota in notas:
    if nota >= 7.0:
        aprovados.append(nota)

print("\n=== Etapa 2: Notas Aprovadas ===")
print("Notas:", aprovados)
print(f"Total de aprovados: {len(aprovados)}")

consulta = "carla silva"
consulta_padronizada = consulta.strip().title()

encontrado = False
for nome in nomes_padronizados:
    if nome == consulta_padronizada:
        encontrado = True
        break

print("\n=== Etapa 3: Verificação de Presença ===")
if encontrado:
    print(f'"{consulta_padronizada}" está PRESENTE na lista.')
else:
    print(f'"{consulta_padronizada}" está AUSENTE na lista.')

print("\n========== RELATÓRIO FINAL ==========")
print(f"Total de estudantes cadastrados : {len(nomes_padronizados)}")
print(f"Total de notas lançadas         : {len(notas)}")
print(f"Total de aprovações             : {len(aprovados)}")
print(f"Total de reprovações            : {len(notas) - len(aprovados)}")
print(f"Estudante consultado            : {consulta_padronizada}")
print(f"Status de presença              : {'Presente' if encontrado else 'Ausente'}")
print("=====================================")

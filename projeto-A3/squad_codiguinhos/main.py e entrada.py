from motor_outliers import calcular_metricas
from auditoria_viz import exibir_relatorio
from engine_benford import analisar_lei_benford, Transacao 

notas_brutas = [100, 100, 100, 100, 100, 100, 100, 100, 100, 2000]
notas_fiscais = []

for nota in notas_brutas:
    if nota > 0:
        notas_fiscais.append(nota)

print(f"Notas processadas: {notas_fiscais}")
print("-" * 30)


media, variancia, qtd = calcular_metricas(notas_fiscais)
print("-" * 30)
print(f"Média calculada: {media:.2f}")


limite_de_corte = 500.00
exibir_relatorio(notas_fiscais, limite_de_corte)
print("-" * 30)



print("=== ANÁLISE DA LEI DE BENFORD ===")


lista_transacoes_benford = []
for i, valor in enumerate(notas_fiscais):
 
    t = Transacao(id_transacao=i, conta_contabil="101", valor=valor, data="2026-01-01")
    lista_transacoes_benford.append(t)


frequencias = analisar_lei_benford(lista_transacoes_benford)

print("Dígito | Frequência Real")
for digito, porcentagem in frequencias.items():
    print(f"   {digito}   | {porcentagem}%")

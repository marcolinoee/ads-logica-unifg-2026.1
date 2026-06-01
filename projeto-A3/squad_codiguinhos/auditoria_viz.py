def exibir_relatorio(notas_fiscais, limite_seguranca):
    print("--- RELATÓRIO DE AUDITORIA ---")
    for i, nota in enumerate(notas_fiscais):
        if nota > limite_seguranca:
            print(f"ID {i}: R$ {nota} -> SUSPEITO!")
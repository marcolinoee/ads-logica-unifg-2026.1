def calcular_mrp(receita, demanda, semana_entrega, componentes):
    resultado = []
    
    for nome_componente, qtd_receita in receita.items():
        dados_comp = componentes[nome_componente]
        
        nec_bruta = demanda * qtd_receita
        nec_liquida = nec_bruta - dados_comp['estoque']
        
        semana_compra = semana_entrega - dados_comp['lead_time']
        
        if semana_compra < 1:
            semana_compra = 1
            print(f"\033[33mATENÇÃO: Prazo de entrega do {nome_componente} é muito longo! Compra atrasada.\033[m")
            return resultado
        
        resultado.append({
            'nome': nome_componente,
            'necessidade_bruta': nec_bruta,
            'necessidade': nec_liquida,
            'semana_compra': semana_compra,
            'estoque_atual': dados_comp['estoque']
        })
    
    return resultado

def validar_viabilidade(receita, semana_entrega, componentes):
    problemas = []
    for nome_componente, qtd_receita in receita.items():
        dados_comp = componentes[nome_componente]
        semana_necessaria = semana_entrega - dados_comp['lead_time']
        
        if semana_necessaria < 1:
            problemas.append(
                f"Prazo de entrega do {nome_componente} ({dados_comp['lead_time']} sem.) incompatível."
            )
    return (len(problemas) == 0, problemas)
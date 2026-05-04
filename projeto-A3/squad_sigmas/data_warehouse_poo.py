def criar_venda(linha_limpa):
    return {
        "data": linha_limpa[0],
        "produto": linha_limpa[1],
        "quantidade": linha_limpa[2],
        "valor_unitario": linha_limpa[3],
        "estado": linha_limpa[4]
    }

def get_valor_total(dicionario_venda):
    return dicionario_venda["quantidade"] * dicionario_venda["valor_unitario"]

def mostrar_tudo(banco_de_dados):
    if banco_de_dados:
        for venda in banco_de_dados:
            #print(f"\nvenda: {list(venda.values())}")
            print(f"data: {venda['data']}")
            print(f"produto: {venda['produto']}")
            print(f"quantidade: {venda['quantidade']}")
            print(f"valor: R${venda['valor_unitario']:.2f}")
            print(f"estado: {venda['estado']}")
            
            total = get_valor_total(venda)
            print(f"VALOR TOTAL: R${total:.2f}")
            print("-" * 25)
    else:
        print("Nenhum dado válido foi processado.")
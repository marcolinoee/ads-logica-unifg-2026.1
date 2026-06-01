class Transacao:

    def __init__(self, id_transacao, conta_contabil, valor, data):
        self.id_transacao = id_transacao
        self.conta_contabil = conta_contabil
        self.valor = float(valor)
        self.data = data
        self.suspeito_outlier = False


def analisar_lei_benford(lista_transacoes):
    contagem = {str(i): 0 for i in range(1, 10)}
    total_validos = 0

    for transacao in lista_transacoes:
        valor_str = str(transacao.valor)
        valor_limpo = valor_str.replace('-', '').replace('.', '').strip()
        valor_limpo = valor_limpo.lstrip('0')
        
        if valor_limpo:
            primeiro_digito = valor_limpo[0]
            if primeiro_digito in contagem:
                contagem[primeiro_digito] += 1
                total_validos += 1

    frequencias_reais = {}
    for digito, qtd in contagem.items():
        if total_validos > 0:
            porcentagem = (qtd / total_validos) * 100
        else: 
            porcentagem = 0.0

        frequencias_reais[digito] = round(porcentagem, 1)

    return frequencias_reais



if __name__ == "__main__":
   
    transacoes_teste = [
        Transacao(id_transacao=1, conta_contabil="101", valor=150.00, data="2026-01-01"),
        Transacao(id_transacao=2, conta_contabil="102", valor=12.50, data="2026-01-02"),
        Transacao(id_transacao=3, conta_contabil="101", valor=2300.15, data="2026-01-03"),
        Transacao(id_transacao=4, conta_contabil="103", valor=55.00, data="2026-01-04"),
    ]


    resultado = analisar_lei_benford(transacoes_teste)

    print("=== RESULTADO DA ANÁLISE DE BENFORD ===")
    print(f"Total de transações analisadas: {len(transacoes_teste)}\n")
    
    print("Dígito | Frequência Reizada")
    print("-------|-------------------")
    for digito, porcentagem in resultado.items():
        print(f"   {digito}   | {porcentagem}%")
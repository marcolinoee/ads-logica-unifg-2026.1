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
def calcular_metricas(valores):
    soma = 0
    for valor in valores:
        soma = soma + valor
    media = soma / len(valores)

    soma_extra = 0 
    for valor in valores:
        soma_extra = soma_extra + (valor - media)**2
    variancia = soma_extra / len(valores)

    desvio = variancia ** 0.5
    limite = media + (3 * desvio)
    
   
    for valor in valores:
        if valor >= limite:
            z_score = (valor - media) / desvio
            print(f"ALERTA DE FRAUDE !!! Valor encontrado : {valor}")
            print(f"Z-Score deste valor: {z_score:.2f}")

    
    return media, variancia, len(valores)
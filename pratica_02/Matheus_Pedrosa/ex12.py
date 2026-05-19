while True:
    valor = float(input('Digite o valor da compra (ou -1 para encerrar): R$ '))
    if valor == -1:
        break
    if valor < 50:
        classificacao = 'sem desconto'
    elif valor <= 100:
        classificacao = 'desconto básico'
    else:
        classificacao = 'desconto especial'
    print(f'Compra de R$ {valor:.2f}: {classificacao}')
print('Encerrando classificação de compras.')

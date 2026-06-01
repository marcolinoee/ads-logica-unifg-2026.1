import os
from data import save_point

def separação():
    print("=" * 60)

def menu_principal(lista):
    separação()
    print("\033[1mSISTEMA MRP\033[m".center(64))
    separação()
    print(f"{lista[0]} - \033[1mNovo Pedido de Produção\033[m")
    print(f"{lista[1]} - \033[1mVer Cronograma de Compras\033[m")
    print(f"{lista[2]} - \033[1mConsultar Estoque Atual\033[m")         
    print(f"{lista[3]} - \033[1mHistórico de Pedidos\033[m")         
    print(f"{lista[4]} - \033[1mHistórico de Movimentações\033[m")         
    print(f"{lista[5]} - \033[1mSair\033[m")
    separação()
    while True:
        try:
            opçao = input("Digite a sua opção: ")
            if opçao not in ["1","2","3","4","5","6"] or not opçao:
                print("\033[31mOPÇÃO INEXISTENTE!\033[m")
                continue
        except KeyboardInterrupt:
            print("\033[31mERRO, NÃO INTERROMPA FORÇADAMENTE O PROGRAMA!\033[m")
            continue
        break
    return opçao

def criar_pedido(produtos): 
    separação()
    print("\033[33mPRODUTOS DISPONIVEIS\033[m".center(65))
    separação()
    print("-" * 60)
    for i , produto in enumerate(produtos.keys(), 1):
        print(f"\033[34m{i} : {produto}\033[m")
    print("-" * 60)
    while True:
        try:
            escolha_produto = input("Nome do Produto: ").title().strip()
            if escolha_produto not in produtos:
                print("\033[31mPRODUTO NÃO ENCONTRADO!\033[m")
                continue
        except KeyboardInterrupt:
            print("\033[31mERRO, NÃO INTERROMPA FORÇADAMENTE O PROGRAMA!\033[m") 
            continue   
        break
    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("\033[31mDIGITE UM NÚMERO VÁLIDO!\033[m")
                continue
        except (ValueError,KeyboardInterrupt):
            print("\033[31mDIGITE UM NÚMERO VÁLIDO!\033[m")
            continue
        break
    while True:
        try:
            semana = int(input("Semana de entrega(1-8): "))
            if semana < 1 or semana > 8:
                print("\033[33mA SEMANA DEVE ESTAR ENTRE 1 E 8!\033[m")
                continue
        except (ValueError,KeyboardInterrupt):
            print("\033[31mDIGITE UM NÚMERO VÁLIDO!\033[m")
            continue
        break
    return {'produto': escolha_produto, 'quantidade': quantidade, 'semana': semana}
    
def processar_pedido(componentes, produtos):

    pedido = criar_pedido(produtos)
    if not pedido:
        print("\033[31mERRO NO RECONHECIMENTO DO PEDIDO!\033[m")
        return   
    from engine import motor_calculos
    ordens = motor_calculos.calcular_mrp(
        produtos[pedido['produto']],
        pedido['quantidade'],
        pedido['semana'],
        componentes
    )
    if len(ordens) < 4:
        print("\033[31mERRO NO PRAZO DE ENTREGA!\033[m")
    else:
        separação()
        print("RESUMO DO PEDIDO".center(60))
        separação()
        print(f"Produto: {pedido['produto']}")
        print(f"Quantidade: {pedido['quantidade']}")
        print(f"Entrega: Semana {pedido['semana']}")
        print(f"ORDENS DE COMPRAS GERADAS:")
        separação()
        for ordem in ordens:
            if ordem['necessidade'] > 0:
                print(f"{ordem['nome']:<15} | {ordem['necessidade']:>5} un. | {ordem['semana_compra']} sem.")
            else:
                print("\033[31mERRO, NÃO EXISTE NECESSIDADE DE COMPRAR MAIS COMPONENTES!\033[m")
                break
        separação()
        while True:    
            confirmação =  input("Corfirmar (s/n): ").strip().lower()
            if confirmação not in ["s", "n"]:
                print("\033[31mERRO, DIGITE S(SIM) OU N(NÃO)!\033[m")
                continue
            break
        if confirmação == "s":
            save_point.adicionar_pedido(pedido['produto'],pedido['quantidade'],pedido['semana'])

            for ordem in ordens:
                if ordem['necessidade'] > 0:
                    save_point.adicionar_ordem_compra(
                        ordem['nome'],
                        ordem['necessidade'],
                        ordem['semana_compra']
                    )
                if componentes[ordem['nome']]['estoque'] < ordem['necessidade_bruta']:
                    componentes[ordem['nome']]['estoque'] = 0
                else:
                    componentes[ordem['nome']]['estoque'] -= ordem['necessidade_bruta']

                save_point.adicionar_movimentaçao(
                    "CONSUMO",
                    ordem['nome'],
                    ordem['necessidade_bruta'],
                    f"Pedido {pedido['produto']} {pedido['quantidade']}un"
                )

            save_point.salvar_estoque(componentes)                                                      

            print("\033[32mPedido confirmado e salvo com sucesso!\033[m")
        else:
            print("\033[31mPedido cancelado!\033[m")            

def exibir_estoque(componentes):
    separação()
    print("ESTOQUE ATUAL".center(50))
    separação()
    for nome, dados in componentes.items():
        print(f"{nome:<15} | {dados['estoque']:>5} un. | Prazo: {dados['lead_time']} sem.")
    separação()
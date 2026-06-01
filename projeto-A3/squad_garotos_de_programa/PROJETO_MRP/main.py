import plano_mestre
from data import save_point
import os
os.system("clear" if os.name != "nt" else "cls")
arquivo = save_point.iniciar_arquivo()

componentes = save_point.carregar_componentes()
produtos = save_point.carregar_produtos()

while True:    
    escolha = plano_mestre.menu_principal([1,2,3,4,5,6])
    if escolha == "1":
        plano_mestre.processar_pedido(componentes=componentes, produtos=produtos) #Adicionar novos pedidos/confirmação desse novo pedido
    if escolha == "2":
        pass #Ver cronograma de compras
    if escolha == "3":
        plano_mestre.exibir_estoque(componentes) #Exibe o estoque atual de itens
    if escolha == "4":
        save_point.exibir_historico() #Exibe o histórico de pedidos em formato de um print utilizando tuplas
    if escolha == "5":
        pass #Exibe o histórico de movimentações(quantos componentes foram comprados para tal produto e produtos foram pedidos)
    if escolha == "6":
        plano_mestre.separação()
        print("ENCERRANDO PROGRAMA!".center(60))
        plano_mestre.separação()
        break

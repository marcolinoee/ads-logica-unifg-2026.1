import cli_ingestao
import etl_transformer
import data_warehouse_poo

banco_de_dados = []

texto_bruto = cli_ingestao.coletar_dados()

matriz = etl_transformer.limpar_dados(texto_bruto)

if matriz:
    for linha in matriz:
        venda_dicionario = data_warehouse_poo.criar_venda(linha)
        banco_de_dados.append(venda_dicionario)

print("\n--- EXIBINDO DADOS ---")
data_warehouse_poo.mostrar_tudo(banco_de_dados)
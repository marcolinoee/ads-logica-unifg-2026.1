import plano_mestre

arquivo = "estoque.txt"

def iniciar_arquivo():
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            pass
    except FileNotFoundError:
        with open(arquivo, 'w', encoding='utf-8') as f:
            
            f.write("===== COMPONENTES =====\n")
            f.write("Assento|20un|1sem\n")
            f.write("Encosto|0un|2sem\n")
            f.write("Eixo|10un|1sem\n")
            f.write("Rodinhas|40un|3sem\n\n")
            
            f.write("===== PRODUTOS =====\n")
            f.write("Cadeira|Assento:1un;Encosto:1un;Eixo:1un;Rodinhas:5un\n\n")

            f.write("===== HISTORICO PEDIDOS =====\n")
            f.write("===== ORDENS COMPRA =====\n")
            f.write("===== MOVIMENTAÇÕES =====\n")

def carregar_componentes():
    
    componentes = {}
    
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    lendo_linhas = False
    for linha in linhas:
        linha = linha.strip()

        if linha == "===== COMPONENTES =====":
            lendo_linhas = True
            continue
        elif linha.startswith("====="):
            lendo_linhas = False
            continue
        if lendo_linhas and linha:
            partes = linha.split("|")
            nome = partes[0]
            estoque = int(partes[1].replace("un", "").strip())
            lead_time = int(partes[2].replace("sem", "").strip())
            componentes[nome] = {'estoque': estoque, 'lead_time': lead_time}
    
    return componentes  

def carregar_produtos():
    
    produtos = {}
    
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    lendo_produtos = False
    
    for linha in linhas:
        linha = linha.strip()
        if linha == "===== PRODUTOS =====":
            lendo_produtos = True
            continue
        elif linha.startswith("====="):
            lendo_produtos = False
            continue

        if lendo_produtos and linha:
            partes = linha.split("|")
            nome_produto = partes[0]
            receita_str = partes[1]
            receita = {}
            for item in receita_str.split(";"):
                comp, qntd = item.split(":")
                receita[comp] = int(qntd.replace("un", ""))
            produtos[nome_produto] = receita
    return produtos

def salvar_estoque(componentes):

    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    novas_linhas = []
    lendo_componentes = False

    for linha in linhas:
        if linha.strip() == "===== COMPONENTES =====":
            novas_linhas.append(linha)
            lendo_componentes = True
            for nome, dados in componentes.items():
                novas_linhas.append(f"{nome}|{dados['estoque']}|{dados['lead_time']}\n")
            continue
        if lendo_componentes and linha.strip().startswith("====="):
            lendo_componentes = False
        if not lendo_componentes:
            novas_linhas.append(linha)
        
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.writelines(novas_linhas)

def adicionar_pedido(produto, quantidade, semana):

    linha = f"{produto}|{quantidade}un|{semana}sem\n"

    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    conteudo = conteudo.replace(
        "===== HISTORICO PEDIDOS =====\n",
        f"===== HISTORICO PEDIDOS =====\n{linha}"
    )
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

def adicionar_ordem_compra(componente, quantidade, semana):
    linha = f"{componente}|{quantidade}un|{semana}sem\n"
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    conteudo = conteudo.replace(
        "===== ORDENS COMPRA =====\n",
        f"===== ORDENS COMPRA =====\n{linha}"
    )
    
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

def adicionar_movimentaçao(tipo, componente, quantidade, observaçao):
    linha = f"{tipo}|{componente}|{quantidade}un|{observaçao}\n"

    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    conteudo = conteudo.replace(
        "===== MOVIMENTAÇÕES =====\n",
        f"===== MOVIMENTAÇÕES =====\n{linha}"
    )

    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

def exibir_historico():
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    plano_mestre.separação()
    print("HISTÓRICO DE PEDIDOS".center(60))
    plano_mestre.separação()
    
    lendo_historico = False
    for linha in linhas:
        linha = linha.strip()

        if linha == "===== HISTORICO PEDIDOS =====":
            lendo_historico = True
            continue
        elif linha.startswith("====="):
            if lendo_historico:
                break
        if lendo_historico and linha:
            partes = linha.split("|")
            print(f"{partes[0]} - {partes[1].replace("un", "")} un. - Semana {partes[2]}") 
    
    plano_mestre.separação() 

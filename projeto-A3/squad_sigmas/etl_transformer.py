def limpar_dados(bloco_bruto):
    lista = []
    linhas = bloco_bruto.split('\n')

    for linha in linhas:
        if linha.strip() == "":
            continue

        partes = [p.strip() for p in linha.split(",")]

        if "" in partes:
            print("[LOG] Linha descartada: campo vazio.")
            continue

        elif len(partes) < 5:
            print("[LOG] Linha descartada: poucos dados.")
            continue
        elif len(partes) > 5:
            partes = partes[:3] + [",".join(partes[3:-1])] + [partes[-1]]

            if len(partes) != 5:
                print("[LOG] Linha descartada: formato inválido.")
                continue

        try:
            data = partes[0]
            produto = partes[1]
            quantidade = int(partes[2])
            valor = float(partes[3].replace(",", "."))
            estado = partes[4]
            lista.append([data, produto, quantidade, valor, estado])

        except:
            print("[LOG] Linha descartada: erro nos dados.")

    return lista
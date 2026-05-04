def coletar_dados():
    linhas = []
    while True:
        texto = input("Digite os dados (ou FIM para parar): \n")
        if texto == "FIM":
            break
        linhas.append(texto)
    return "\n".join(linhas)
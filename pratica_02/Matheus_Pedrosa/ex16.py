contagem_s = 0
while True:
    resposta = input('Digite S, N ou FIM para encerrar: ').strip().upper()
    if resposta == 'FIM':
        break
    if resposta == 'S':
        contagem_s += 1
print(f'Foram digitados {contagem_s} respostas S.')
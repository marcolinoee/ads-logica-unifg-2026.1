# Desafio do Download
tamanho_mb = float(input("escreva o tamanho do megabyte:"))
velocidade_mpbs = float(input("escreva a velocidade da net:"))

megabyte = ( tamanho_mb * 8.0)

tempo_seg = (tamanho_mb) / (velocidade_mpbs/8)
min_inteiros = int (tempo_seg//60)
tempo_restante = int (tempo_seg % 60)

print( min_inteiros, "minutos e", tempo_seg,"segundos")
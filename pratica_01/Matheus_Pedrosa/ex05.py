tamanho_mb = float(input('Digite o tamanho do arquivo em MB: '))
velocidade_mbps = float(input('Digite a velocidade da internet em Mbps: '))

tempo_segundos = (velocidade_mbps > 0) and tamanho_mb / (velocidade_mbps / 8)
minutos = int((tempo_segundos or 0) // 60)
segundos = int((tempo_segundos or 0) % 60)

print((velocidade_mbps <= 0 and 'Velocidade deve ser maior que zero.') or f'{minutos} minutos e {segundos} segundos')

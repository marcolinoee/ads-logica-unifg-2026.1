tamanho_mb = float(input("Tamanho do arquivo em MB: "))
velocidade_mbps = float(input("Velocidade em Mbps: "))
tempo_segundos = tamanho_mb / (velocidade_mbps / 8)
minutos = int(tempo_segundos) // 60
segundos = int(tempo_segundos) % 60
print(f"Tempo estimado: {minutos} minuto(s) e {segundos} segundo(s).")

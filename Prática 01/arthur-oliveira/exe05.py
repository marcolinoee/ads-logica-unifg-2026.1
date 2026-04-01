tamanho_mb = float(input("Digite o tamanho do arquivo (MB): "))
mbps = float(input("Digite a velocidade da internet (Mbps): "))


tamanho_megabits = tamanho_mb * 8


tempo_segundos = tamanho_megabits / mbps


minutos = int(tempo_segundos // 60)
segundos = int(tempo_segundos % 60)

print(f"Tempo estimado: {minutos} minutos e {segundos} segundos")
tamanho_mb = float(input("Digite o tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Digite a velocidade da internet (Mbps): "))

velocidade_real = velocidade_mbps / 8

tempo_total_segundos = tamanho_mb / velocidade_real

minutos = int(tempo_total_segundos // 60)
segundos_restantes = int(tempo_total_segundos % 60)


print("=" * 30)
print(f"Tempo estimado: {minutos} minutos e {segundos_restantes} segundos.")
print("baixando")
print("=" * 30)

tamanho_arquivo = float(input(f"Qual o tamanho do arquivo(em MB)? "))
velocidade_internet_por_segundo = float(input("Qual a velocidade de conexão da internet por segundos(em Mbps)? "))

tempo_em_segundos = tamanho_arquivo / (velocidade_internet_por_segundo/8)
em_minutos = tempo_em_segundos // 60
minutos_inteiros = int(em_minutos)
segundos_restantes = tempo_em_segundos % 60
segundos_restantes_inteiros = int(segundos_restantes)


print(f"O tempo estimado pro download é: {minutos_inteiros} minutos e {segundos_restantes_inteiros} segundos")
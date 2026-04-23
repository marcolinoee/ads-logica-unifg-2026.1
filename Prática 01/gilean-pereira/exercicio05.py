tamanho_arq = float(input("Digite o tamanho do arquivo:"))
velocidadde_net = float(input("Digite a velocidade:"))

temp_sec = tamanho_arq / (velocidadde_net/8)
temp_min = temp_sec // 60
temp_rest = temp_sec % 60

print (f"Seu arquivo demorá {temp_min:.1f} e {temp_rest:.1f} para concluir")
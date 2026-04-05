tamanhoArquivo = float(input("Digite o tamanho do arquivo em Mb: "))
velocidadeConexao = float(input("Digite a velocidade da conexão de Internet em Megabits por segundo (Mbps): "))

tempoS = tamanhoArquivo / (velocidadeConexao / 8)
minutoInteiro = tempoS // 60
segundosRestantes = tempoS % 60

print("-=-" * 15)
print("\033[1;32mCarregamento em andamento...\033[m")
print(f"\033[1;34m{minutoInteiro:.1f} minutos e {segundosRestantes:.1f} segundos\033[m")
print("-=-" * 15)
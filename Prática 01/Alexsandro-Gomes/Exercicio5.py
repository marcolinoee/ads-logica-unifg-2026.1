TamanhoArquivo = int(input("Qual o tamanho do seu arquivo em MB : "))
VelocidadeConexao = float(input("Qual a velocidade de sua internet em MB por segundo : "))
TempoSegundo = TamanhoArquivo/(VelocidadeConexao/8)
MinutosInteiros = TempoSegundo//60
SegundosRestante = TempoSegundo%60

print(f"Tempo restante de downlaod {MinutosInteiros:.1f} Minutos e {SegundosRestante:.1f} Segundos")
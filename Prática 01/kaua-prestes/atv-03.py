total_fatias = int(input("Digite o número de fatias: \n"))
num_pessoas = int(input("Digite a quantidade de pessoas: \n"))

fatias_pessoa = total_fatias // num_pessoas
sobra = total_fatias % num_pessoas

print(f"Cada um vai pegar {fatias_pessoa} fatias de pizza")
print(f"Vai sobrar {sobra} fatias na caixa")
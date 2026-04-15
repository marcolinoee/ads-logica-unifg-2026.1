total_fatias = int(input("Qual o número total de fatias de pizza? "))
quantidade_de_programadores = int(input("São quantos programadores na equipe? "))

fatias_por_pessoa = total_fatias // quantidade_de_programadores
sobra = total_fatias % quantidade_de_programadores

print(f"Cada programador irá comer {fatias_por_pessoa} fatias")
print(f"Irá sobrar na caixa {sobra} fatias")
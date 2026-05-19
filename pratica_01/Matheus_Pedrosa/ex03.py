total_fatias = int(input('Digite o número total de fatias: '))
programadores = int(input('Digite o número de programadores: '))

fatias_pessoa = total_fatias // programadores
sobra = total_fatias % programadores

print(f'Cada pessoa recebe {fatias_pessoa} fatias.')
print(f'Sobraram {sobra} fatias.')
seguir = "S"
sair = "N"
valor_total = 0

while (seguir != sair):
    
    valor_compra = float(input("Valor do produto:"))
    valor_total += valor_compra
    seguir = input("Deseja continuar? (S/N):")


print(F"Seu valor total:{valor_total}")
contador_par = 0

for numero in range (1,9):
    contagem =int (input ("Digite um numero:"))
    if (contagem % 2 == 0):
        contador_par = contador_par + contagem
print (f"soma dos pares é {contador_par}")
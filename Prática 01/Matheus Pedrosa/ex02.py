horasTrabalho = int(input("Qual é a quantidade de horas de trabalho? ")) 
horasProjeto = int(input("Qual é a estimativa de horas para concluir o projeto? "))

valorBruto = horasProjeto * horasProjeto
imposto = valorBruto * 0.15
valorLiquido = valorBruto - imposto

print("\033[1;33m-=-" * 11)
print("     VALOR DO PROJETO")
print("-=-" * 11)

print(f"\033[mO valor bruto:   \033[34mR${valorBruto:.2f}\033[m")
print(f"O valor do imposto:   \033[34mR${imposto:.2f}\033[m")
print(f"O valor liquído:   \033[34mR${valorLiquido:.2f}\033[m")
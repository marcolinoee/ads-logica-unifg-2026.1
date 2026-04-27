#para essa atividade escolhi o Exercício 08

soma_pares = 0
for i in range(1,9):
    numero = int(input(f"Digite o {i}° valor: "))
    
    if numero % 2 == 0:
        soma_pares += numero

print(f"A soma dos pares é: {soma_pares}")

#Ficou melhor com o "For" deu menos linhas e menos chances de errar porque o for ele ja faz a repetição dos números por si só e com o "While" eu teria que ter o trabalho de colocar o contador pra fazer o sistema rodar.
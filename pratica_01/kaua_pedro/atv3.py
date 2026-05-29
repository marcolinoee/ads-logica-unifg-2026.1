# fatias de pizza 
qnt_pizza = int(input("escreva quantas pizza tem no total:"))
pessoas = int(input("escreva a quantidade de pessoas:"))
              
fatias_por_pessoas= (qnt_pizza/pessoas)
sobra = (qnt_pizza % pessoas)

print("sobrou", sobra, "pedaços de pizza")
print("mas cada pessoas comeram", fatias_por_pessoas,"pedaços de pizza")

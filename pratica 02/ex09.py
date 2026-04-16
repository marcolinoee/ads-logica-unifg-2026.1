salario=float(input("digite o salario:"))
if salario<=1500:
  reajuste=0.15
elif salario<=3000:
  reajuste=0.10
else:
  reajuste=0.05
  novo_salario=salario+(salario*reajuste)
  print("novo salario:",novo_salario)

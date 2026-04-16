opcao=-1
while opcao!=0:
  print("\n1-somar")
  print("2-subtrair")
  print("0-sair")
  opcaint(input("escolha uma opcao:"))
  if opcao==1:
  a=float(input("numero 1:"))
  b=float(input("numero 2:"))
  print("resultado:",a+b)
elif opcao==2:
a=float(input("numero1:"))
b=float(input("numero2:"))
print("resultado:",a-b)
print("programa encerrado!")

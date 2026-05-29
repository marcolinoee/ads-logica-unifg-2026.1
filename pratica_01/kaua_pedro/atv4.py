#Verificador de Acesso
idade = int(input("escreva sua idade: "))
experiencia = int(input("escreva sua experiencia:"))

acesso = bool((idade > 18)*(experiencia > 2))

print(f"acesso liberado:{acesso}")
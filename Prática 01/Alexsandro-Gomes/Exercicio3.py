NumeroDeFatias = int(input("Numero de fatias da pizza : "))
NumeroDePessoas = int(input("Numero de programadores na equipe : "))
FatiasPorPessoa = NumeroDeFatias//NumeroDePessoas 
Sobra = NumeroDeFatias%NumeroDePessoas

print(f"Fatias por programador : {FatiasPorPessoa} ")
print(f"Fatias que sobraram : {Sobra} ")
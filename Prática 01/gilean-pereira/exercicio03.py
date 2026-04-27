total_fatias = int(input("numeros de fatias:"))
total_pessoas = int(input ("numeros de pessoas:"))

fatias_pessoas = total_fatias // total_pessoas
fatias_sobraram = total_fatias % total_pessoas

print ("fatias por pessoas",fatias_pessoas)
print ("fatias que sobrarm",fatias_sobraram)
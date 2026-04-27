Follow = "S"
Exit = "N"
Total_Value = 0
while (Follow != Exit):     
    Buy_Value = float(input("Valor do produto:"))
    Total_Value += Buy_Value
    Follow = input("Deseja continuar? (S/N):")
print(f"Valor total:{Total_Value}")

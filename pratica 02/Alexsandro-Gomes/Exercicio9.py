Salary = int(input("Qual o seu salario : "))
if (Salary<=1500):
    increase = 0.15
elif (Salary>1500) or (Salary<=3000):
    increase = 0.10
else:
    increase = 0.05
increasement = Salary*increase
NewSalary = increasement + Salary
print(f"O rejuste do seu salario e {increasement} sendo assim no final {NewSalary} ")

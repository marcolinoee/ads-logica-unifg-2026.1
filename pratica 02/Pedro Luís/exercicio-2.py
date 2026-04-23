import os 
os.system("cls" if os.name == "nt" else "clear")

while True:
    try:
        idade = int(input("Digite a sua idade: "))
    except ValueError:
        print("Digite apenas números inteiros!")
        continue
    break
if idade < 18:
    print("Você é menor de idade.")
elif 18 <= idade <= 59:
    print("Você é maior de idade.")
else:
    print("Você é idoso.") 
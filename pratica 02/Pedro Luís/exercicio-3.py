import os 
os.system("cls" if os.name == "nt" else "clear")

for i in range(1, 21):
    if i % 2 == 0:
        print(f"\033[32m{i} é par\033[m")
    else:
        print(f"\033[31m{i} é impar\033[m")
import os 
os.system("cls" if os.name == "nt" else "clear")

while True:
    senha = input("Digite a senha: ").strip().lower()
    if senha == "acesso":
        print("\033[32mOLÁ USUÁRIO!\033[m")
        break
    else:
        print("\033[31mSENHA ERRADA!\033[m")
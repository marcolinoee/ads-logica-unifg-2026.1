# ex16.py
contador_sim = 0
resposta = ""
while resposta != "FIM":
    resposta = input("S, N ou FIM: ").strip().upper()
    if resposta == "S":
        contador_sim += 1
print(f"Total de SIM: {contador_sim}")
# While e ideal pois nao sabemos quantas respostas o usuario vai digitar

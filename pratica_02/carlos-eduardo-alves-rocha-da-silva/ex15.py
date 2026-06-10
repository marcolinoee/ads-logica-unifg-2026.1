# ex15.py
maior_nota = None
for i in range(1, 6):
    nota = float(input(f"Digite a {i} nota: "))
    if maior_nota is None or nota > maior_nota:
        maior_nota = nota
print(f"Maior nota: {maior_nota}")
# While seria adequado se nao soubessemos quantas notas seriam lidas

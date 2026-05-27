def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

media = calcular_media(n1, n2)
situacao = verificar_situacao(media)

print(f"Média: {media}")
print(situacao)
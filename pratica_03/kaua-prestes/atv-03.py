def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
print(f"A média é: {calcular_media(n1, n2)}")

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
situacao = verificar_situacao(calcular_media(n1, n2))
print(f"A situação do aluno é: {situacao}")
def ler_notas():
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    return notas

def calcular_media(notas):
    soma = 0
    quantidade = 0

    for nota in notas:
        soma += nota
        quantidade += 1

    media = soma / quantidade
    return media

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
def exibir_resultado(media, situacao):
    print(f"A média é: {media:.2f}")
    print(f"A situação do aluno é: {situacao}")

notas = ler_notas()
media = calcular_media(notas)   
situacao = verificar_situacao(media)
exibir_resultado(media, situacao)
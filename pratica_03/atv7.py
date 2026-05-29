def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_situacao(media_final):
    if media_final >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


n1 = 8
n2 = 6

media = calcular_media(n1, n2)
verificar_situacao(media)
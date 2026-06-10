def ler_notas():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    return n1, n2

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_resultado(nome, media, situacao):
    print("=" * 30)
    print(f"Aluno:    {nome}")
    print(f"Media:    {media:.1f}")
    print(f"Situacao: {situacao}")
    print("=" * 30)

nome = input("Digite o nome do aluno: ")
n1, n2 = ler_notas()
media = calcular_media(n1, n2)
situacao = verificar_situacao(media)
exibir_resultado(nome, media, situacao)

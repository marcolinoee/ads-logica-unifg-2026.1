def verificar_situacao(nota):
    if nota >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
nota = float(input("Digite a nota do aluno: "))
situacao = verificar_situacao(nota)
print(f"A situação do aluno é: {situacao}")
for x in range(15):
    nota = int(input(f"Aluno {x+1}, digite a nota (0 a 10): "))

    if nota > 10:
        print("Erro: A nota não pode ser maior que 10.\n")
    elif nota < 0:
        print("Erro: A nota não pode ser menor que 0.\n")
    else:
        print(f"Nota {nota} registrada com sucesso para o aluno {x}!\n")

print("Fim do Programa! Todas as 15 notas foram processadas.")

# Achei um pouco mais simples!
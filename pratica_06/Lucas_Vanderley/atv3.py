class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

aluno = Estudante("Lucas", "12345")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(9.0)
print(f"Notas adicionadas: {aluno.notas}")
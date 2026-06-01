class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):

        return "Aprovado" if self.calcular_media() >= 7.0 else "Recuperação"

aluno = Estudante("Lucas", "123")
aluno.adicionar_nota(6.5)
aluno.adicionar_nota(7.0)
print(f"Média: {aluno.calcular_media():.2f} - Situação: {aluno.situacao()}")
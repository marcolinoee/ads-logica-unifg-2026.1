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

aluno1 = Estudante("Ana Silva", "202601")
aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(9.5)

aluno2 = Estudante("Bruno Souza", "202602")
aluno2.adicionar_nota(6.0)
aluno2.adicionar_nota(7.0)

print(f"{aluno1.nome} - Média: {aluno1.calcular_media():.2f}")
print(f"{aluno2.nome} - Média: {aluno2.calcular_media():.2f}")
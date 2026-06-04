class Turma:
    def __init__(self):
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

    def relatorio(self):
        for e in self.estudantes:
            print(e.nome, e.calcular_media(), e.situacao())
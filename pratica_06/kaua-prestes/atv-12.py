class Turma:
    def __init__(self):
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

    def media_geral(self):
        if len(self.estudantes) == 0:
            return 0
        soma = 0
        for e in self.estudantes:
            soma += e.calcular_media()
        return soma / len(self.estudantes)
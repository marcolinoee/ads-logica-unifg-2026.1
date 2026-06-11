class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
    def adicionar_nota(self, nota):
        self.notas.append(nota)
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
class Turma:
    def __init__(self):
        self.estudantes = []
    def matricular(self, estudante):
        self.estudantes.append(estudante)
    def media_geral(self):
        if len(self.estudantes) == 0:
            return 0
        return sum(e.calcular_media() for e in self.estudantes) / len(self.estudantes)
t = Turma()
e1 = Estudante("Carlos", "001")
e1.adicionar_nota(8.0)
e2 = Estudante("Ana", "002")
e2.adicionar_nota(6.0)
t.matricular(e1)
t.matricular(e2)
print(f"Média geral: {t.media_geral():.2f}")

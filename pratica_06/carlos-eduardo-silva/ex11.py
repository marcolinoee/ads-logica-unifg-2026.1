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
t = Turma()
e1 = Estudante("Carlos", "001")
e2 = Estudante("Ana", "002")
t.matricular(e1)
t.matricular(e2)
print(f"Estudantes: {len(t.estudantes)}")

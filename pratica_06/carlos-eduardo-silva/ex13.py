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
    def situacao(self):
        return "Aprovado" if self.calcular_media() >= 7 else "Recuperação"
class Turma:
    def __init__(self):
        self.estudantes = []
    def matricular(self, estudante):
        self.estudantes.append(estudante)
    def relatorio(self):
        for e in self.estudantes:
            print(f"{e.nome} - Média: {e.calcular_media():.2f} - {e.situacao()}")
t = Turma()
e1 = Estudante("Carlos", "001")
e1.adicionar_nota(8.0)
e2 = Estudante("Ana", "002")
e2.adicionar_nota(6.0)
t.matricular(e1)
t.matricular(e2)
t.relatorio()

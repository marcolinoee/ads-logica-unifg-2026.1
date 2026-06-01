class Estudante:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def situacao(self):
        return "Aprovado" if self.calcular_media() >= 7.0 else "Recuperação"

class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

    def exibir_relatorio(self):
        print(f"--- RELATÓRIO DA TURMA: {self.nome_turma} ---")

        for estudante in self.estudantes:
            print(f"Nome: {estudante.nome} | Média: {estudante.calcular_media():.2f} | Situação: {estudante.situacao()}")


a1 = Estudante("Carla")
a1.adicionar_nota(9.5)

a2 = Estudante("Diego")
a2.adicionar_nota(5.0)

sala = Turma("Programação OO")
sala.matricular(a1)
sala.matricular(a2)

sala.exibir_relatorio()
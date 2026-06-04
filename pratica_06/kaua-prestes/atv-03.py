class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

e = Estudante("Ana", "001")
e.adicionar_nota(8)
e.adicionar_nota(7)
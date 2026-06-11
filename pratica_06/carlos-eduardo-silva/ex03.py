class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
    def adicionar_nota(self, nota):
        self.notas.append(nota)
e1 = Estudante("Carlos", "001")
e1.adicionar_nota(8.0)
e1.adicionar_nota(7.5)
print(e1.notas)

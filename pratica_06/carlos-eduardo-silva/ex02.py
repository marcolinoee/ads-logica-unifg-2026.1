class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
e1 = Estudante("Carlos", "001")
print(e1.notas)

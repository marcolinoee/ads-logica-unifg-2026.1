class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
e1 = Estudante("Carlos", "001")
print(e1.nome, e1.matricula)

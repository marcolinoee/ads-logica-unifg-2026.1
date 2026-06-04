class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)


e1 = Estudante("Ana", "001")
e2 = Estudante("João", "002")

e1.adicionar_nota(10)
e2.adicionar_nota(5)

print(e1.nome, e1.notas)
print(e2.nome, e2.notas)
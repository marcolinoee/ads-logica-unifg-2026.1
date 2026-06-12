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
e1 = Estudante("Carlos", "001")
e2 = Estudante("Ana", "002")
e1.adicionar_nota(9.0)
e2.adicionar_nota(6.0)
print(f"{e1.nome} - Média: {e1.calcular_media():.2f}")
print(f"{e2.nome} - Média: {e2.calcular_media():.2f}")

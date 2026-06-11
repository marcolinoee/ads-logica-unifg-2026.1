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
e1.adicionar_nota(8.0)
e1.adicionar_nota(7.0)
print(f"Média: {e1.calcular_media():.2f}")

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
        if self.calcular_media() >= 7:
            return "Aprovado"
        return "Recuperação"
e1 = Estudante("Carlos", "001")
e1.adicionar_nota(8.0)
e1.adicionar_nota(6.0)
print(f"{e1.nome} - {e1.situacao()}")

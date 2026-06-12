# Código com erro - sem self
class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
    def adicionar_nota(self, nota):
        # Erro seria: notas.append(nota) sem self
        # Correto:
        self.notas.append(nota)
e1 = Estudante("Carlos", "001")
e1.adicionar_nota(9.0)
print(f"Notas: {e1.notas}")

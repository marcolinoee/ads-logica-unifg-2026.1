class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
    def adicionar_nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("Nota inválida! Deve ser entre 0 e 10.")
        self.notas.append(nota)
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
e1 = Estudante("Carlos", "001")
try:
    e1.adicionar_nota(11)
except ValueError as e:
    print(e)
e1.adicionar_nota(8.0)
print(f"Notas: {e1.notas}")

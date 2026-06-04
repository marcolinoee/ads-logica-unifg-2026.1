class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("Nota inválida")
        self.notas.append(nota)
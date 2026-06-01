class Estudante:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

    def calcular_media_geral(self):
        if not self.estudantes:
            return 0
        
        soma_medias = sum(estudante.calcular_media() for estudante in self.estudantes)
        return soma_medias / len(self.estudantes)


a1 = Estudante("Lucas")
a1.adicionar_nota(8.0)

a2 = Estudante("Bruno")
a2.adicionar_nota(6.0)

minha_turma = Turma("Algoritmos")
minha_turma.matricular(a1)
minha_turma.matricular(a2)

print(f"Média geral da turma: {minha_turma.calcular_media_geral():.2f}")
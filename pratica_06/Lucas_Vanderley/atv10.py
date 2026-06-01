class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.estudantes = [] 

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)


minha_turma = Turma("Algoritmos II")


minha_turma.adicionar_estudante(Estudante("Ana", "01"))
minha_turma.adicionar_estudante(Estudante("Lucas", "02"))

print(f"Turma: {minha_turma.nome_turma}")
print(f"Quantidade de alunos matriculados: {len(minha_turma.estudantes)}")
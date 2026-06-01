class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

turma_python = Turma("Python Avançado")
aluno_novo = Estudante("Lucas Vanderley", "202609")

turma_python.matricular(aluno_novo)
print(f"Alunos matriculados na turma {turma_python.nome_turma}: {len(turma_python.estudantes)}")
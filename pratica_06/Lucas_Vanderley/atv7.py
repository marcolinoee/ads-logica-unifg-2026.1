class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
      
        if not (0 <= nota <= 10):
            raise ValueError("A nota deve estar entre 0 e 10.")
        self.notas.append(nota)


aluno = Estudante("Lucas", "123")
try:
    aluno.adicionar_nota(11.5)  
except ValueError as e:
    print(f"Erro capturado com sucesso: {e}")
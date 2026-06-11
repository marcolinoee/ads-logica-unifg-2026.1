# Atributo de classe: compartilhado por todos os objetos
# Atributo de instância: exclusivo de cada objeto
class Produto:
    imposto_padrao = 0.1  # atributo de classe
    def __init__(self, nome, preco):
        self.nome = nome   # atributo de instância
        self.preco = preco # atributo de instância

p1 = Produto("Caderno", 10.0)
p2 = Produto("Caneta", 2.0)

print(f"Imposto p1: {p1.imposto_padrao}")
print(f"Imposto p2: {p2.imposto_padrao}")

Produto.imposto_padrao = 0.2
print(f"Após alterar classe:")
print(f"Imposto p1: {p1.imposto_padrao}")
print(f"Imposto p2: {p2.imposto_padrao}")

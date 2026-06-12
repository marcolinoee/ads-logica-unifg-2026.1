class Produto:
    imposto_padrao = 0.1
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
p1 = Produto("Caderno", 20.0)
print(f"Imposto padrão: {Produto.imposto_padrao}")
print(f"Produto: {p1.nome} - R${p1.preco}")

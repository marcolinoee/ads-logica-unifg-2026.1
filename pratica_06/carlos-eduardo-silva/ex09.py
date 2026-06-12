class Produto:
    imposto_padrao = 0.1
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def preco_com_imposto(self):
        return self.preco + (self.preco * Produto.imposto_padrao)
p1 = Produto("Caderno", 20.0)
print(f"{p1.nome} - Preço com imposto: R${p1.preco_com_imposto():.2f}")

class Produto:
    imposto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def preco_com_imposto(self):
        return self.preco * (1 + Produto.imposto_padrao)
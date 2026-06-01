class Produto:
    imposto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def preco_com_imposto(self):
        return self.preco * (1 + Produto.imposto_padrao)


p = Produto("Celular", 2000.00)
print(f"Preço original: R$ {p.preco:.2f}")
print(f"Preço com imposto: R$ {p.preco_com_imposto():.2f}")
class Produto:
  
    imposto_padrao = 0.10

    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco

p1 = Produto("Notebook", 3500.00)
print(f"Produto: {p1.nome} | Imposto padrão da classe: {Produto.imposto_padrao}")
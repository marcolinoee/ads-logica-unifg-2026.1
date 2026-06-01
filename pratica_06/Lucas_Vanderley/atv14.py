# CÓDIGO INCORRETO (Exemplo do problema):
# class Conta:
#     def __init__(self, titular, saldo_inicial):
#         titular = titular          <- Erro: Variável local, some após o __init__
#         saldo = saldo_inicial      <- Erro: Não vira atributo do objeto

# CÓDIGO CORRIGIDO (Uso correto do self):
class Conta:
    def __init__(self, titular, saldo_inicial):

        self.titular = titular          
        self.saldo = saldo_inicial      

    def exibir_dados(self):

        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")


minha_conta = Conta("Lucas", 1500.00)
minha_conta.exibir_dados()
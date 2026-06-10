# Analise do codigo original:
# x = 10  -> variavel GLOBAL (definida fora da funcao)
# y = 5   -> variavel LOCAL (definida dentro da funcao)
# Se tentarmos usar 'y' fora da funcao, ocorre NameError,
# pois y so existe enquanto a funcao esta sendo executada.

x = 10

def teste():
    y = 5
    return x + y

print(teste())  # 15

# Exemplo proprio:
contador = 100  # global

def incrementar():
    valor = 1   # local
    return contador + valor

print(incrementar())  # 101
# print(valor)  # isso causaria NameError

# Erro: ZeroDivisionError - divisao por zero
# Ocorre porque matematicamente nao e possivel dividir por zero.

def dividir(a, b):
    if b == 0:
        return "Erro: nao e possivel dividir por zero."
    return a / b

print(dividir(10, 2))   # normal
print(dividir(10, 0))   # caso limitrofe com mensagem amigavel

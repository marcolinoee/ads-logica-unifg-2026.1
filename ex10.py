# Funcao analisada:
def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total

# PARTE A - Teste de mesa com calcular_total(50, 2):
# preco=50 | quantidade=2 | subtotal=100 | desconto=10.0 | total=90.0
print("Teste de mesa calcular_total(50, 2):", calcular_total(50, 2))

# PARTE B - Casos de teste
print(calcular_total(50, 2))    # caso normal -> 90.0
print(calcular_total(100, 3))   # caso normal -> 270.0
print(calcular_total(0, 5))     # caso limitrofe (preco zero) -> 0.0
print(calcular_total(99999, 1000))  # caso extremo -> 89999100.0

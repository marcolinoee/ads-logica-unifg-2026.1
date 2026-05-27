def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total
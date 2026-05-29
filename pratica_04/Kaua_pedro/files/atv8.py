itens = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]

contagem_mouse = 0
contagem_teclado = 0

for item in itens:
    if item == "mouse":
        contagem_mouse += 1
    if item == "teclado":
        contagem_teclado += 1

print(f'"mouse" aparece {contagem_mouse} vez(es) na lista.')
print(f'"teclado" aparece {contagem_teclado} vez(es) na lista.')

contagem_monitor = 0
for item in itens:
    if item == "monitor":
        contagem_monitor += 1

print(f'"monitor" aparece {contagem_monitor} vez(es) na lista.')

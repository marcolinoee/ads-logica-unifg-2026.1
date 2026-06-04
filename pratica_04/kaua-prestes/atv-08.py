itens = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]

cont_mouse = 0
cont_teclado = 0

for item in itens:
    if item == "mouse":
        cont_mouse += 1
    if item == "teclado":
        cont_teclado += 1

print(f"Mouse aparece {cont_mouse} vezes")
print(f"Teclado aparece {cont_teclado} vezes")
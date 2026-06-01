itens = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]

mouse = 0
teclado = 0

for item in itens:
    if item == "mouse":
        mouse + 1
        if item == "teclado":
            teclado + 1

print(f"Teclado aparece {1} vez!")
print(f"Mouse aparece {1} vez!")
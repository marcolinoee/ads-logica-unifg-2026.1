# ex13.py
# Problema: contador += 1 fazia crescer infinitamente
# Correcao: usar -= 1
contador = 10
while contador > 0:
    print(contador)
    contador -= 1
print("Contagem encerrada!")

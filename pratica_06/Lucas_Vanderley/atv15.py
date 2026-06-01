class Carro:
    rodas = 4  

    def __init__(self, modelo):
        self.modelo = modelo

carro1 = Carro("Fusca")
carro2 = Carro("Ferrari")

print(f"{carro1.modelo} tem {carro1.rodas} rodas.")
print(f"{carro2.modelo} tem {carro2.rodas} rodas.\n")

Carro.rodas = 6  

print("--- Após modificar a Classe Carro ---")
print(f"{carro1.modelo} agora reflete: {carro1.rodas} rodas.")
print(f"{carro2.modelo} agora reflete: {carro2.rodas} rodas.")
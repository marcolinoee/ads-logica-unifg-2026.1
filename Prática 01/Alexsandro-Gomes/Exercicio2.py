ValorEntrada = float(input("Valor cobrado por hora : "))
HorasTrabalhadas = float(input("Qual sua estimava em horas : "))
ValorBruto = ValorEntrada*HorasTrabalhadas
Imposto = ValorBruto*0.15
Valorliquido = ValorBruto - Imposto

print(f"O valor total do bruto do projeto {ValorBruto}, Valor dos impostos {Imposto},e o valor final {Valorliquido} ")
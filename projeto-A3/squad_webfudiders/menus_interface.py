def ler_numero_decimal(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem)
        try:
            valor = float(entrada)
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"O valor deve estar entre {minimo} e {maximo}.")
        except ValueError:
            print("Erro! Entrada inválida. Digite um número decimal.")  


def ler_inteiro(mensagem, minimo, maximo):  
    while True:
        entrada = input(mensagem)
        try:
            valor = int(entrada)
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Escolha uma opção entre {minimo} e {maximo}.")  
        except ValueError:  
            print("Erro! Entrada inválida. Digitar número inteiro.")


def exibir_menu_principal():
    print("\n" + "="*40)
    print("SISTEMA LOGÍSTICO UNIVERSITÁRIO")
    print("="*40)
    print("1. Cadastrar Nova Aula (Motor de Alocação)")
    print("2. Testar Inserção de Notas (Interface Segura)")
    print("3. Sair")
    print("="*40)
    return ler_inteiro("Escolha uma opção (1-3):", 1, 3) 
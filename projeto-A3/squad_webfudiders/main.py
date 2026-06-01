from menus_interface import iniciar_sistema


def mostrar_cabecalho():
    print("=" * 70)
    print("           ERP EDUCACIONAL - GESTÃO E ALOCAÇÃO")
    print("=" * 70)
    print("Sistema acadêmico para controle de horários e turmas")
    print("Projeto A3 - Fundamentos da Programação")
    print("=" * 70)


def mostrar_funcionalidades():
    print("\nFUNCIONALIDADES DO SISTEMA")
    print("-" * 70)
    print("1. Cadastrar aulas informando professor, turma, disciplina, dia e bloco")
    print("2. Impedir choque de horário para professores")
    print("3. Impedir choque de horário para turmas")
    print("4. Controlar limite de carga horária por professor")
    print("5. Listar aulas cadastradas")
    print("6. Validar a grade de horários cadastrada")
    print("-" * 70)


def mostrar_regras_resumidas():
    print("\nREGRAS DE ALOCAÇÃO")
    print("-" * 70)
    print("Regra 1: Um professor não pode ter duas aulas no mesmo dia e bloco.")
    print("Regra 2: Uma turma não pode ter duas disciplinas no mesmo dia e bloco.")
    print("Regra 3: O professor não pode ultrapassar sua carga horária máxima.")
    print("-" * 70)


def confirmar_inicio():
    while True:
        resposta = input("\nDeseja iniciar o sistema agora? (S/N): ").strip().upper()

        if resposta == "S":
            return True

        if resposta == "N":
            return False

        print("Opção inválida. Digite apenas S para sim ou N para não.")


def executar_programa():
    try:
        mostrar_cabecalho()
        mostrar_funcionalidades()
        mostrar_regras_resumidas()

        iniciar = confirmar_inicio()

        if iniciar:
            print("\nIniciando o menu principal...")
            iniciar_sistema()
        else:
            print("\nSistema encerrado antes de iniciar o menu.")

    except KeyboardInterrupt:
        print("\n\nSistema interrompido pelo usuário.")
        print("Encerrando com segurança...")

    except Exception as erro:
        print("\nOcorreu um erro inesperado.")
        print(f"Detalhes: {erro}")
        print("O sistema será encerrado.")


def main():
    executar_programa()


if __name__ == "__main__":
    main()
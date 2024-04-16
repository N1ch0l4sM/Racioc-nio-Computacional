

menus_1 = {1:"Estudantes", 2:"Professores", 3:"Disciplinas", 4:"Turmas", 5:"Matrículas"}
menus_2 = {1: "Incluir", 2: "Listar", 3: "Editar", 4: "Excluir", 9: "Voltar"}
opcao = 0
estudantes = []

while opcao != 9:
    print("\n---- MENU PRINCIPAL ----\n")

    while True:
        for key, value in menus_1.items():
            print(f"({key}) - Gerenciar {value}.")
        print("(9) - Sair.")
        try:
            opcao = int(input("\nInforme o numero a opção desejada: "))
            if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5 or opcao == 9:
                break
            else:
                print("O número deve estar entre 1 e 5 ou 9.")
        except ValueError:
            print("Valor inválido")
        except:
            print("Outro tipo de erro ocorreu!")
        print("")

    if opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
        print("EM DESENVOLVIMENTO.")
        continue
    
    if opcao == 9:
        print("Saindo do programa.")
        break

    while True:
        while True:
            if opcao == 1:
                print(f"\n---- MENU {menus_1[opcao]} ----\n")
                for key, value in menus_2.items():
                    print(f"({key}) - {value}.")
            try:
                opcao_2 = int(input("\nInforme o numero da ação desejada: "))
                if opcao_2 == 1 or opcao_2 == 2 or opcao_2 == 3 or opcao_2 == 4 or opcao_2 == 9:
                    break
                else:
                    print("O número deve estar entre 1 e 4 ou 9.")
            except ValueError:
                print("Valor inválido")
            except:
                print("Outro tipo de erro ocorreu!")
            print("")

        if opcao_2 == 1:
            print("==== Inclusão ====")
            estudante = {}
            cod = int(input("Informe o código do estudante: "))
            nome = input("Informe o nome do estudante: ")
            cpf = input("Informe o CPF do estudante: ")
            estudante["codigo"] = cod
            estudante["nome"] = nome
            estudante["cpf"] = cpf
            estudantes.append(estudante)
            input("Pressione ENTER para continuar.\n")

        elif opcao_2 == 2:
            print("==== Listagem ====")
            for estudante in estudantes:
                print(estudante)
            input("Pressione ENTER para continuar.")

        elif opcao_2 == 3:
            print("==== Edição ====")
            cod_editar = int(input("Informe o código do estudante que sera editado: "))
            cod = int(input("Informe novo código do estudante: "))
            nome = input("Informe o nome do estudante: ")
            cpf = input("Informe o CPF do estudante: ")
            estudante_editar = None
            for estudante in estudantes:
                if estudante["codigo"] == cod_editar:
                    estudante_editar = estudante
                    break 
            if estudante_editar == None: 
                print("Estudante não encontrado.")
                continue
            else:
                estudante_editar["codigo"] = cod
                estudante_editar["nome"] = nome
                estudante_editar["cpf"] = cpf
                
        elif opcao_2 == 4:
            print("==== Excluir ====")
            cod_excluir = int(input("Informe o código do estudante que sera excluido: "))
            estudante_excluir = None
            for estudante in estudantes:
                if estudante["codigo"] == cod_excluir:
                    estudante_excluir = estudante
                    break 
            if estudante_excluir == None: 
                print("Estudante não encontrado.")
                continue
            else:
                estudantes.remove(estudante_excluir)
                
        elif opcao_2 == 9:
            print("==== Voltando ====")
            break

print("Fim do programa.\n")

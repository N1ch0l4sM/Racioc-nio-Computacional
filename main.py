import json

def mostrar_menu_principal():
    print("\n---- MENU PRINCIPAL ----\n")
    print("1 - Estudantes")
    print("2 - Professores")
    print("3 - Disciplinas")
    print("4 - Turmas")
    print("5 - Matrículas")
    print("9 - Sair")

def mostrar_menu_operacoes():
    print("1 - Incluir")
    print("2 - Listar")
    print("3 - Editar")
    print("4 - Excluir")
    print("9 - Voltar")

def incluir_estudante():
    print("==== Inclusão ====")
    estudante = {}
    cod = int(input("Informe o código do estudante: "))
    nome = input("Informe o nome do estudante: ")
    cpf = input("Informe o CPF do estudante: ")
    estudante["codigo"] = cod
    estudante["nome"] = nome
    estudante["cpf"] = cpf
    estudantes = carregar_lista_estudantes()
    estudantes.append(estudante)
    salvar_lista_estudantes(estudantes)
    input("Pressione ENTER para continuar.\n")

def listar_estudantes(estudantes):
    print("==== Listagem ====")
    for estudante in estudantes:
        print(estudante)
    input("Pressione ENTER para continuar.\n")

def editar_estudante(estudantes):
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
    else:
        estudante_editar["codigo"] = cod
        estudante_editar["nome"] = nome
        estudante_editar["cpf"] = cpf

def excluir_estudante(estudantes):
    print("==== Excluir ====")
    cod_excluir = int(input("Informe o código do estudante que sera excluido: "))
    estudante_excluir = None
    for estudante in estudantes:
        if estudante["codigo"] == cod_excluir:
            estudante_excluir = estudante
            break 
    if estudante_excluir == None: 
        print("Estudante não encontrado.")
    else:
        estudantes.remove(estudante_excluir)
        print("Estudante excluido com sucesso.")
                
def salvar_lista_estudantes(estudantes):
    with open("estudantes.json", "w") as f:
        json.dump(estudantes, f)

def carregar_lista_estudantes():
    try:
        with open("estudantes.json", "r") as f:
            return json.load(f)
    except:
        return []
    
menus_1 = {1:"Estudantes", 2:"Professores", 3:"Disciplinas", 4:"Turmas", 5:"Matrículas"}
menus_2 = {1: "Incluir", 2: "Listar", 3: "Editar", 4: "Excluir", 9: "Voltar"}
opcao = 0

while opcao != 9:
    
    while True:
        mostrar_menu_principal()
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
                mostrar_menu_operacoes()
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
            incluir_estudante()

        elif opcao_2 == 2:
            estudantes = carregar_lista_estudantes()
            if len(estudantes) == 0:
                print("Nenhum estudante cadastrado.")
            else:
                listar_estudantes(estudantes)

        elif opcao_2 == 3:
            if len(estudantes) == 0:
                print("Nenhum estudante cadastrado.")
            else:
                editar_estudante(estudantes)
                
        elif opcao_2 == 4:
            if len(estudantes) == 0:
                print("Nenhum estudante cadastrado.")
            else:  
                excluir_estudante(estudantes)

        elif opcao_2 == 9:
            print("==== Voltando ====")
            break

print("Fim do programa.\n")

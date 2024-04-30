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

def incluir(nome):
    print("==== Inclusão ====")
    item = {}
    lista = carregar_lista(nome)
    if nome == "estudantes":
        cod = int(input("Informe o código do estudante: "))
        nome = input("Informe o nome do estudante: ")
        cpf = input("Informe o CPF do estudante: ")
        item["codigo"] = cod
        item["nome"] = nome
        item["cpf"] = cpf
        if item in lista:
            print("Estudante já cadastrado.")
        else:
            lista.append(item)
            salvar_lista("estudantes", lista)
    elif nome == "professores":
        cod = int(input("Informe o código do professor: "))
        nome = input("Informe o nome do professor: ")
        cpf = input("Informe o CPF do professor: ")
        item["codigo"] = cod
        item["nome"] = nome
        item["cpf"] = cpf
        if item in lista:
            print("Professor já cadastrado.")
        else:
            lista.append(item)
            salvar_lista("professores", lista)
    elif nome == "disciplinas":
        cod = int(input("Informe o código da disciplina: "))
        nome = input("Informe o nome da disciplina: ")
        item["codigo"] = cod
        item["nome"] = nome
        if item in lista:
            print("Disciplina já cadastrada.")
        else:
            lista.append(item)
            salvar_lista("disciplinas", lista)
    elif nome == "turmas":
        cod = int(input("Informe o código da turma: "))
        cod_prof = int(input("Informe o código do professor: "))
        cod_disc = int(input("Informe o código da disciplina: "))
        item["codigo"] = cod
        item["prof"] = cod_prof
        item["disc"] = cod_disc
        if item in lista:
            print("Turma já cadastrada.")
        else:
            lista.append(item)
            salvar_lista("turmas", lista)
    elif nome == "matriculas":
        cod_est = int(input("Informe o código do estudante: "))
        cod_turma = int(input("Informe o código da turma: "))
        item["estudante"] = cod_est
        item["turma"] = cod_turma
        if item in lista:
            print("Matricula já cadastrada.")
        else:
            lista.append(item)
            salvar_lista("matriculas", lista)
    else:
        print("Lista não encontrada.")
    input("Pressione ENTER para continuar.\n")


def listar(nome):
    lista= carregar_lista(nome)
    print("==== Listagem ====")
    if len(lista) == 0:
        print("Nenhum item cadastrado.")
    else:
        for item in lista:
            print(item)
    input("Pressione ENTER para continuar.\n")

def editar_estudante():
    estudantes = carregar_lista("estudantes")
    if estudantes == []:
        print("Lista vazia.")
    else:
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
            salvar_lista('estudantes', estudantes)

def editar_professor():
    professores = carregar_lista("professores")
    if professores == []:
        print("Lista vazia.")
    else:
        print("==== Edição ====")
        cod_editar = int(input("Informe o código do professor que sera editado: "))
        cod = int(input("Informe novo código do professor: "))
        nome = input("Informe o nome do professor: ")
        cpf = input("Informe o CPF do professor: ")
        professor_editar = None
        for professor in professores:
            if professor["codigo"] == cod_editar:
                professor_editar = professor
                break 
        if professor_editar == None: 
            print("Professor não encontrado.")
        else:
            professor_editar["codigo"] = cod
            professor_editar["nome"] = nome
            professor_editar["cpf"] = cpf
            salvar_lista('professores', professores)

def editar_disciplina():
    disciplinas = carregar_lista("disciplinas")
    if disciplinas == []:
        print("Lista vazia.")
    else:
        print("==== Edição ====")
        cod_editar = int(input("Informe o código da disciplina que sera editada: "))
        cod = int(input("Informe novo código da disciplina: "))
        nome = input("Informe o nome da disciplina: ")
        disciplina_editar = None
        for disciplina in disciplinas:
            if disciplina["codigo"] == cod_editar:
                disciplina_editar = disciplina
                break 
        if disciplina_editar == None: 
            print("Disciplina não encontrada.")
        else:
            disciplina_editar["codigo"] = cod
            disciplina_editar["nome"] = nome
            salvar_lista('disciplinas', disciplinas)

def editar_turma():
    turmas = carregar_lista("turmas")
    if turmas == []:
        print("Lista vazia.")
    else:
        print("==== Edição ====")
        cod_editar = int(input("Informe o código da turma que sera editada: "))
        cod = int(input("Informe novo código da turma: "))
        cod_prof = int(input("Informe o novo código do professor: "))
        cod_disc = int(input("Informe o novo código da disciplina: "))
        turma_editar = None
        for turma in turmas:
            if turma["codigo"] == cod_editar:
                turma_editar = turma
                break 
        if turma_editar == None: 
            print("Turma não encontrada.")
        else:
            turma_editar["codigo"] = cod
            turma_editar["prof"] = cod_prof
            turma_editar["disc"] = cod_disc
            salvar_lista('turmas', turmas)

def editar_matricula():
    matriculas = carregar_lista("matriculas")
    if matriculas == []:
        print("Lista vazia.")
    else:
        print("==== Edição ====")
        cod_editar = int(input("Informe o código do estudante que sera editado: "))
        cod_est = int(input("Informe o novo código do estudante: "))
        cod_turma = int(input("Informe o novo código da turma: "))
        matricula_editar = None
        for matricula in matriculas:
            if matricula["estudante"] == cod_editar:
                matricula_editar = matricula
                break 
        if matricula_editar == None: 
            print("Matricula não encontrada.")
        else:
            matricula_editar["estudante"] = cod_est
            matricula_editar["turma"] = cod_turma
            salvar_lista('matriculas', matriculas)


def excluir(nome):
    lista = carregar_lista(nome)
    if lista == []:
        print("Lista vazia.")
    else:
        print("==== Excluir ====")
        cod_excluir = int(input("Informe o código do item que sera excluido: "))
        item_excluir = None
        for item in lista:
            if nome == "matriculas":
                if item["estudante"] == cod_excluir:
                    item_excluir = item
                    break
            else:
                if item["codigo"] == cod_excluir:
                    item_excluir = item
                    break 
        if item_excluir == None: 
            print("Não encontrado.")
        else:
            lista.remove(item_excluir)
            print("Excluido com sucesso.")
            salvar_lista(nome, lista)
                    

def salvar_lista(nome, lista):
    with open(nome+".json", "w") as f:
        json.dump(lista, f)


def carregar_lista(nome):
    try:
        with open(nome+".json", "r") as f:
            return json.load(f)
    except:
        return []
    
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
    
    if opcao == 9:
        print("Saindo do programa.")
        break

    while True:
        while True:
            if opcao == 1:
                print(f"\n---- MENU Estudantes ----\n")
                mostrar_menu_operacoes()
            elif opcao == 2:
                print(f"\n---- MENU Professores ----\n")
                mostrar_menu_operacoes()
            elif opcao == 3:
                print(f"\n---- MENU Disciplinas ----\n")
                mostrar_menu_operacoes()
            elif opcao == 4:
                print(f"\n---- MENU Turmas ----\n")
                mostrar_menu_operacoes()
            elif opcao == 5:
                print(f"\n---- MENU Matrículas ----\n")
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
            if opcao == 1:
                incluir("estudantes")
            elif opcao == 2:
                incluir("professores")
            elif opcao == 3:
                incluir("disciplinas")
            elif opcao == 4:
                incluir("turmas")
            elif opcao == 5:
                incluir("matriculas")

        elif opcao_2 == 2:
            if opcao == 1:
                listar("estudantes")
            elif opcao == 2:
                listar("professores")
            elif opcao == 3:
                listar("disciplinas")
            elif opcao == 4:
                listar("turmas")
            elif opcao == 5:
                listar("matriculas")
            

        elif opcao_2 == 3:
            if opcao == 1:
                editar_estudante()
            elif opcao == 2:
                editar_professor()
            elif opcao == 3:
                editar_disciplina()
            elif opcao == 4:
                editar_turma()
            elif opcao == 5:
                editar_matricula()
            
                
        elif opcao_2 == 4:
            if opcao == 1:
                excluir("estudantes")
            elif opcao == 2:
                excluir("professores")
            elif opcao == 3:
                excluir("disciplinas")
            elif opcao == 4:
                excluir("turmas")
            elif opcao == 5:
                excluir("matriculas")
            

        elif opcao_2 == 9:
            print("==== Voltando ====")
            break

print("Fim do programa.\n")

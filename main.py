# programa de tasks utilizando mysql

import crudpython as c

# Menu
menu = True

while True:
    print("\n------Menu:------")
    print("1. Cadastrar Tarefa")
    print("2. Selecionar Todas Tarefas")
    print("3. Modificar tarefa")
    print("4. Deletar Tafera")
    print("0. Sair")
    print("-----------------")

    choice = input("\nDigite sua escolha: ")

    if choice == "1":
        name = input("Nome da tarefa: ")
        description = input("Descrição da tarefa: ")
        c.create_task(name, description)
        print(f"\n✅ Tarefa {name} criada!\n")

    elif choice == "2":
        print("Todas Tarefas!")
        c.readAll_task()

    elif choice == "3":
        nameTask = input("Informe o nome da tarefa que será atualizada: ")
        name = input("Informe o novo nome: ")
        description = input("Informe a nova descrição: ")
        c.update_task(name, description, nameTask)
        print(f"✅ Tarefa {name} atualizada!")
    elif choice == "4":
        id = int(input("Informe o id da tarefa que deseja excluir: "))
        c.delete_task(id)
        print(f"\n❌ Tarefa {id} Excluida!")

    elif choice == "0":
        print("\nPrograma encerrado, até mais!🖐️\n")
        break  # Sair do loop
    else:
        print("Código inválido, Por favor digite novamente")

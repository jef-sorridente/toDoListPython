# programa de tasks utilizando mysql

import crudpython as c

# Menu
menu = True

while True:
    print("\n------Menu:------")
    print("1. Cadastrar Tarefa")
    print("0. Sair")
    print("-----------------")

    choice = input("\nDigite sua escolha: ")

    if choice == "1":
        name = input("Nome da tarefa: ")
        description = input("Descrição da tarefa: ")
        c.create_task(name, description)
        print("✅ Tarefa criada!")
    elif choice == "0":
        break  # Sair do loop
    else:
        print("Código inválido, Por favor digite novamente")

import mysql.connector


# Função para conexão
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="root",
        database="db_todo_list",
    )


# CREATE
def create_task(name, description):

    try:
        conn = get_connection()
        cursor = conn.cursor()
        command = "INSERT INTO tasks (task_name,task_descript) VALUES (%s, %s)"
        cursor.execute(command, (name, description))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"[ERRO] ao inserir: {err}")

    finally:
        cursor.close()
        conn.close()


# READ
def readAll_task():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        command = "SELECT * FROM tasks"
        cursor.execute(command)
        result = cursor.fetchall()

        print("\n📋 Lista de Tarefas:\n")
        for task in result:
            id, name, descript = task
            print(f"Id: {id}")
            print(f"Nome: {name}")
            print(f"Descrição: {descript}")
            print("-" * 60)

    except mysql.connector.Error as err:
        print(f"[ERRO] ao inserir: {err}")

    finally:
        cursor.close()
        conn.close()


# UPDATE
def update_task(name, description, nameTask):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        command = (
            "UPDATE tasks SET task_name = %s, task_descript = %s WHERE task_name = %s"
        )
        cursor.execute(command, (name, description, nameTask))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"[ERRO] ao inserir: {err}")

    finally:
        cursor.close()
        conn.close()


# DELETE
def delete_task(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        command = "DELETE FROM tasks WHERE idtasks = %s"
        cursor.execute(command, (id,))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"[ERRO] ao inserir: {err}")

    finally:
        cursor.close()
        conn.close()

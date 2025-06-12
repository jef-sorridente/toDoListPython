import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost", user="root", password="root", database="db_task"
    )


# CREATE
def create_task(name, description):

    try:
        conn = get_connection()
        cursor = conn.cursor()
        command = 'INSERT INTO tasks (task_name,tasks_descript) VALUES (%s, %s)'
        cursor.execute(command, (name, description))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"[ERRO] ao inserir: {err}")

    finally:
        cursor.close()
        conn.close()


# create_task("Enviar vídeo para a manu", "Enviar vídeo sobre python e mysql.")


# # READ
# def readAll_task():
#     command = "SELECT * FROM tasks"
#     cursor.execute(command)
#     resultado = cursor.fetchall()
#     print(resultado)


# # readAll_task()


# # UPDATE
# def update_task(id, name, description):
#     command = f'UPDATE tasks SET task_name = "{name}", tasks_descript = "{description}" WHERE idtasks = {id}'
#     cursor.execute(command)
#     mydb.commit()


# # update_task(3, "Estudar Java", "Estudar java com o Xissum 2222.")

# # DELETE


# def delete_task(id):
#     command = f"DELETE FROM tasks WHERE idtasks = {id}"
#     cursor.execute(command)
#     mydb.commit()


# delete_task(4)

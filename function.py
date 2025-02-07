import os

def get_todos(filepath="todos.txt"):
    if os.path.exists(filepath):
        # if file exists return todo list
        with open (filepath,"r") as file_local:
            todos_local=file_local.readlines()
        return todos_local
    else:
        with open(filepath,"w") as file:
            return []

def write_todos(todos_arg,filepath="todos.txt"):
    with open(filepath,"w") as file:
        file.writelines(todos_arg)



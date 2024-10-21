FILE_PATH = 'todos.txt'
def get_todos(filepath=FILE_PATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILE_PATH):
    """ Write the to-do item lists in a text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ =="__main__":
    print("Hello")
    print(get_todos())
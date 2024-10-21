#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add or show or complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        """
        file = open('files/todos.txt', 'r')
        todos = file.readlines()
        file.close()
        """

        todos = functions.get_todos()

        todos.append(todo+'\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number-1

            todos = functions.get_todos()

            new_todo =input("Enter new todo: ")

            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is invalid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()

            todo_to_remove = todos[number-1].strip('\n')
            todos.pop(number-1)

            functions.write_todos(todos)
            message = f"Todo : {todo_to_remove} was removed from the Todos list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("You entered an unknown command")


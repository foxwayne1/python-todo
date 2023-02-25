import functions
import time

now = time.strftime('%b %d, %Y - %H:%M:%S')
while True:
    print(f"It is {now}")
    user_action = input('Type ADD, SHOW, EDIT, COMPLETE or EXIT: ').lower()
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos('todos.txt')

        todos.append(todo + '\n')

        functions.write_todos(todos, 'todos.txt')

    elif user_action.startswith('show'):

        todos = functions.get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos('todos.txt')

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, 'todos.txt')

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos('todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(number - 1)

            functions.write_todos(todos, 'todos.txt')

            message = f"Todo: {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print('There is no item with that number')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid.')

print('Bye')

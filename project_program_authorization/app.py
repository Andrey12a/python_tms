from getters import user_input
from validators import check_dataa
from storage import users


def app():
    while True:
        name = user_input('Enter name: ')
        password = user_input('Enter password: ')
        if name == 'exit':
            break
        response = check_dataa(name, password, users)
        if response:
            print(f'hello {name}')
            break
        print('Данные не верны')


app()

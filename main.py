admin_login = 'admin'
admin_password = '12345'


def login():
    log = input('введите логин: ')
    password = input('введите пароль: ')
    if log == admin_login and password == admin_password:
        return True
    else:
        return False


def main_menu():
    while True:
        choice = input('1 - admin, 2 - user')
        if choice == '1':
            if login():
                admin_menu()
        if choice == '2':
            user_menu()





def user_menu():
    pass

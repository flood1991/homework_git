authors = {}




def create_article(user):
    article = {'title': input('Введите заголовок: '),
               'text': input('Введите текст: ')}
    user['articles'].append(article)
    print(client)

def check_articles(func):
    def wrapper(*args):
        if client['articles']:
            func(*args)
        else:
            print(f"У {client['login']} нет статтей ")
                # quit('your list is empty')
    return wrapper


@check_articles
def read_all(user):
        for num, value in enumerate(user['articles'], 1):
            print(f"Статья {num} - {value['title']}")


@check_articles
def choose_article(user):
    pass

@check_articles
def read_article(number, user):
    pass

@check_articles
def update_article(number, user):
    pass

@check_articles
def delete_article(number, user):
    pass


def registration():
    user = {'login': input('Введите логин: '),
            'password': input('Введите пароль: '),
            'articles': []}
    if authors.get(user['login']):
        print('пользователь существует')
    else:
        authors.setdefault(user['login'], user)


def login():
    log_in = input('login: ')
    password = input('password: ')
    try:
        if authors[log_in]['login'] == log_in and authors[log_in]['password'] == password:
            user = authors[log_in]
            return user
    except:
        print('Invalid login or password')






def author_menu(user):
    while True:
        choice = input(f'''
        1 create,
        2 read all,
        3 read article,
        4 update,
        5 delete:''')
        if choice == '1':
            create_article(client)
        if choice == '2':
            read_all(client)
        if choice == '3':
            number = choose_article(client)
            if number != None:
                read_article(number, client)
        if choice == '4':
            number = choose_article(client)
            if number != None:
                update_article(number, client)
        if choice == '5':
            number = choose_article(client)
            if number != None:
                delete_article(number, client)
        if choice == '6':
            break


while True:
    choice = input('1 - login,2 -registration: ')
    if choice == '1':
        client = login()
        if client:
            author_menu(client)
    if choice == '2':
        registration()

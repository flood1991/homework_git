# Task 1-2-3
# -------------------------------------------------------------------------------------------------------
def read(user):
    with open(f"{user}_notepad.txt", 'a') as f:
        f.write('')
    with open(f"{user}_notepad.txt", 'r') as f:
        print(f.read())
def write(user):
    text =input('enter something ')
    with open(f"{user}_notepad.txt", 'a') as f:
        f.write(text+'\n')
def clear(user):
    with open(f"{user}_notepad.txt", 'w') as f:
        f.write('')
def menu():
    while True:
        choice = input('1-read,2 - write,3 - clear,4 exit: ')
        if choice =='1':
            read(user)
        if choice =='2':
            write(user)
        if choice =='3':
            clear(user)
        if choice =='4':
            break

file_users = 'users.txt'
with open(file_users, 'a') as f:
    f.write('')


def registration():
    reg_log = input('enter login: ')
    reg_password = input('enter password: ')
    with open(file_users, 'r') as f:
        users = f.readlines()
        if users:
            for user in users:
                user = user.strip()
                log = user.split(':')[0]
                if reg_log == log:
                    print('Такой пользователь уже есть')
                    break
                elif reg_log and reg_password:
                    print('Вы успешно зарегистрированны')
                    with open(file_users, 'a') as f:
                        f.write(f'{reg_log}:{reg_password}\n')
                    break                
            else:
                print('Вы не ввели данные')
        else:
            print('Вы успешно зарегистрированны')
            with open(file_users, 'a') as f:
                f.write(f'{reg_log}:{reg_password}\n')


def login():
    user_login = input('enter login: ')
    user_password = input('enter password: ')
    with open(file_users, 'r') as f:
        users = f.readlines()
        for user in users:
            user = user.strip()
            log = user.split(':')[0]
            password = user.split(':')[1]
            if user_login == log and user_password == password:
                print('you are entered')
                return log
        else:
            print('wrong login or password')

while True:
    choice = input('1-reg,2-login,3-exit: ')
    if choice == '1':
        registration()
    if choice == '2':
        user = login()
        if user:
            menu()
    if choice == '3':
        break
# ----------------------------------------------------------------------------------------------------------------------------------------


# Task 4
my_articles = 'my_articles.txt'
with open(my_articles, 'a') as f:
    f.write('')

def check(func):
    def wrapper(*args):
        if my_articles:
            func(*args)
        else:
            quit("you haven't saved articles")
    return wrapper


def choice(func):
    def wrapper():
        choice = int(input('Введите номер: ')) - 1
        try:
            func(choice)
        except:
            print('Нет такой статьи')
    return wrapper


def create_article():
    article = {'title': input('Введите заголовок: '),
              'text': input('Введите текст: ')}
    with open (my_articles, 'a') as f:
        f.write(f"{article['title']}:{article['text']}\n")


@check
def list_articles():
    with open (my_articles,'r') as f:
        articles = f.readlines()
    for number, article in enumerate(articles,1):
        print(f"{number} - {article.strip()}")


@check
@choice
def read_article(number=0):
    with open (my_articles,'r') as f:
        article = f.readlines()
        print(f'''
            Заголовок - {article[number].split(':')[0]}, 
            Текст - {article[number].split(':')[1]}
            ''')



@check
@choice
def update_article(number=0):
    with open (my_articles,'r') as f:
        articles = f.readlines()
    with open (my_articles,'w') as f:
        for article in articles:
            if article != articles[number]:
                f.write(article)
            else:
                article = {'title': input('Введите новый заголовок: '),
                            'text': input('Введите новый текст: ')}
                articles[number] = f.write(f"{article['title']}:{article['text']}\n")


@check
@choice
def delete_article(number=0):
    with open (my_articles,'r') as f:
        articles = f.readlines()
    with open (my_articles,'w') as f:
        for article in articles:
            if article != articles[number]:
                f.write(article)





def admin_menu():
    print('You are admin')
    while True:
        choice = input('1 create, 2 read all, 3 read one, '
                       '4 update, 5 delete, 6 exit:')
        if choice == '1':
            create_article()
        if choice == '2':
            list_articles()
        if choice == '3':
            read_article()
        if choice == '4':
            update_article()
        if choice == '5':
            delete_article()
        if choice == '6':
            break


admin_menu()
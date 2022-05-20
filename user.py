import admin
def rate_article():
    pass

def user_menu():
    while True:
        choice = input('1,2,3,4')
        if choice == '1':
            admin.list_articles()
        if choice == '2':
            number = admin.choose_article()
            if number != None:
                admin.read_article(number)
        if choice == '3':
            rate_article()
        if choice == '4':
            break
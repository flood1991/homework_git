from client import test_exists, right_input

tests = []



@test_exists(tests)
@right_input(tests)
def choose_test():
    list_tests()
    choice = int(input('Выберите номер: '))
    return choice


def create_test():
    test = {'name': input('enter test name: '),
            'text': input('enter question: '),
            'answers': input('через , ответы: '),
            'right answer': input('right number: '),
            'score': int(input('сколько балов за ответ: '))}
    tests.append(test)


@test_exists(tests)
def list_tests():
    for num, test in enumerate(tests,1):
        print(f"""{num}Название - {test['name']}""")



def read_test(test_number):
    test = tests[test_number]
    print(f"""text - {test['text']}
    'answers' - {test['answers']}
    'right answer' - {test['right answer']}
    'score' - {test['score']}""")



def update_test(test_number):
    test = tests[test_number]
    test['name'] = input('enter new test name: ')
    test['text'] = input('enter new question: ')
    test['answers'] = input('(через ,) новые ответы: ')
    test['right answer'] = input('right number: ')
    test['score'] = int(input('сколько балов за ответ: '))


def delete_test(test_number):
    del tests[test_number]




def menu():
    while True:
        choice = input('''
        1 - create test,
        2 - list tests,
        3 - read, 
        4 - update, 
        5 -delete,
        6- exit: ''')
        if choice == '1':
            create_test()
        if choice == '2':
            list_tests()
        if choice == '3':
            number = choose_test()
            if number:
                print(f'number - {number}')
                read_test(number-1)
        if choice == '4':
            number = choose_test()
            if number:
                update_test(number)
        if choice == '5':
            number = choose_test()
            if number:
                delete_test(number)
        if choice == '6':
            break
menu()
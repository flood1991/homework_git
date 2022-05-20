def test_exists(tests):
    def tmp(func):
        def wrapper():
            if tests:
                print('-'*40)
                return func()
            else:
                print('Сначала создайте тест')
        return wrapper
    return tmp


def right_input(func):
    def wrapper():
        try:
            return func()
        except Exception:
            print('неверный ввод')
    return wrapper

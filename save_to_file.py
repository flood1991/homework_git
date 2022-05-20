data = []
import pickle
def check_user(login):
    for user in data:
        if user['login'] == login:
            return user
    return False
def registration():
    login = input('login')
    password = input('password')
    if not check_user(login):
        data.append({'login':login, 'password':password})

def login():
    login = input('login')
    password = input('password')
    for user in data:
        if user['login'] == login and user['password'] == password:
            return user
    return False

registration()
text = pickle.dumps(data)
print(text)
text2 = pickle.loads(text)
print(text2)
with open('db.txt', 'ab') as f:
    f.write(text)
with open('db.txt', 'rb') as f:
    print(pickle.loads(f.read()))
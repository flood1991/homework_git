# Task 1

data = [[1, 3, 5, 6], [2, 4, 3, 6, 7], [0, 1, 2], [1, 2, 3, 4, 77]]
print(data[3][4])

data_1 = {'name': 'Name', 'data': [1, 2, 3, [4, 5, 6, {'number': 77}]]}
print(data_1['data'][3][3]['number'])

data_2 = [[], [], [{'numbers': [[], [], [{'number': 77}]]}]]
print(data_2[2][0]['numbers'][2][0]['number'])


# Task 2.1

ospf_route = "     10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
print(f'''Prefix               {ospf_route.split()[0]}
        AD/Metric            {ospf_route.split()[1][1:-1]}
        Next-Hop             {ospf_route.split()[3][:-1]}
        Last update          {ospf_route.split()[4][:-1]}
        Outbound Interface   {ospf_route.split()[5]}''')


# Task 2.2
london_co = {
"r1": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "4451",
"ios": "15.4",
"ip": "10.255.0.1"
},
"r2": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "4451",
"ios": "15.4",
"ip": "10.255.0.2"
},
"sw1": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "3850",
"ios": "3.6.XE",
"ip": "10.255.0.101",
"vlans": "10,20,30",
"routing": True
}
}
choice_device = {'1': 'r1', '2': 'r2', '3': 'sw1'}
device = input('Выберите устройство:1-r1, 2-r2, 3-sw1: ')
print(london_co[choice_device[device]])



# Task 2.3

london_co = {
"r1": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "4451",
"ios": "15.4",
"ip": "10.255.0.1"
},
"r2": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "4451",
"ios": "15.4",
"ip": "10.255.0.2"
},
"sw1": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "3850",
"ios": "3.6.XE",
"ip": "10.255.0.101",
"vlans": "10,20,30",
"routing": True
}
}
'''
def  choice():
    choice = input('Выберите устройство: \n'
                   '1 - r1, 2 - r2, 3 - sw1 ')
    if choice == '1':
        return 'r1'
    if choice == '2':
        return 'r2'
    if choice == '3':
        return 'sw1'


def parametr():
    while True:
        name = int(input('Выберите параметр \n'
          '1 - location; 2 - vendor;\n'
          '3 - model; 4 - ios;\n'
          '5 - ip; 6 - vlans; 7 - routing '))-1

        lst = []
        for key in london_co[device]:
            lst.append(key)
        if name in range(len(lst)):
            return lst[name]
        else:
            break


device = choice()
key = parametr()
if key:
    print(london_co[device][key])
else:
    print('Параметр отсутствует')
'''
choose_device = {'1': 'r1', '2': 'r2', '3': 'sw1'}
choose_param = {'1': 'location', '2': 'vendor', '3': 'model', '4': 'ios',
                '5': 'ip', '6': 'vlans', '7': 'routing'}
device = input('1-r1, 2-r2, 3-sw1: ')
if device == '1' or device == '2':
    param = input('1 - location; 2 - vendor;3 - model; 4 - ios;5 - ip: ')
elif device == '3':
    param = input('1 - location; 2 - vendor;3 - model; 4 - ios;5 - ip;6 - vlans; 7 - routing: ')
else:
    print('wrong device')
print(london_co[choose_device[device]][choose_param[param]])


# Task 3

def add_value(dict):
    field = input('Введите поле: ')
    for key in dict:
        if field == key:
            dict[key] = input('Добавить значение поля: ')
            return dict
    else:
        error = input('Такого поля нет,создать?(1 - да): ')
        if error == '1':
            new_field = dict.setdefault(field)
            return new_field


def user_menus():
    action = input('Выберите действие:\n'
                    '1 Создать резюме - ')
    if action != '1':
        print('Cначала нужно создать резюме')
    else:
        your_cv = {}
        while True:
            action2 = input('Выберите действие:\n'
                            '1 Добавить к резюме поле;\n'
                            '2 Добавить в поле значение;\n'
                            '3 Вывести полученное резюме : ')
            if action2 == '1':
                key = input('Добавить название поля: ')
                your_cv.setdefault(key)
            if action2 == '2':
                add_value(your_cv)
            if action2 == '3':
                return your_cv


print(user_menus())

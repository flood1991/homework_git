# Task 1
mac = 'AAAA:BBBB:CCCC'
print('.'.join(mac.split(':')))


# Task 2
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result = config.split()[4]
print(result.split(','))


# Task 3
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = list(set(vlans))
print(result)


# Task 4
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
set_1 = set(command1.split()[4].split(','))
set_2 = set(command2.split()[4].split(','))
result = set_1 & set_2
print(result)


# Task 5
mac = '02:F7:25:BD:C9:65'
mac = ''.join(mac.split(':'))
new_mac = ''


for i in mac:
    if i.isnumeric():
        i = bin(int(i))
        new_mac += i
    else:
        i = bin(int(i, 16))
        new_mac += i


print(''.join(new_mac.split('0b')))


# Task 6
ip = "192.168.3.1"
ip_list = ip.split('.')
new_ip = ''


for index, value in enumerate(ip_list):
    while len(value) < 10:
        value += ' '
    ip_list[index] = value
    new_ip += bin(int(value))
new_ip = new_ip.strip('0b').split('0b')


for index, value in enumerate(new_ip):
    while len(value) < 10:
        if len(value) < 8:
            value = '0'+value
        else:
            value += ' '
    new_ip[index] = value

print(''.join(ip_list))
print(''.join(new_ip))


# Task 7


def output_list(num):
    num_vlan = input('enter vlan(vlans for trunk): ')
    print(f'interface {interface}')
    for i in choose_mode[mode]:
        print(i.format(num_vlan))


mode = input('enter mode 1- access, 2-trunk: ')
interface = input('enter interface(type and number ex. Gi0/3): ')
access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"]
trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"]
choose_mode = {'1': access_template, '2': trunk_template}


output_list(mode)


# Task 8
user_ip = input('Enter ip (ex - 10.0.43.2): ')
if user_ip.split('.')[0].isnumeric():
    if 1 <= int(user_ip.split('.')[0]) <= 223:
        print('unicast')
    elif 224 <= int(user_ip.split('.')[0]) <= 239:
        print('multicast')
    elif user_ip == '255.255.255.255':
        print('local broadcast')
    elif user_ip == '0.0.0.0':
        print('unassigned')
else:
    print('unused')

# Task 9

data = [1, 3, 4, 5, 2, 3, 43, 12, 123, 23, 3, 4, 56, 7]
elem = len(data)
for i in range(len(data)):
    for j in range(len(data)):
        if data[i] < data[j]:
            data[i], data[j] = data[j], data[i]
print(data)

# Task 10


def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'divide by zero'


number1 = float(input('enter first number'))
number2 = float(input('enter second number'))
choose_action = {'+': plus(number1, number2), '-': minus(number1, number2),
                 '*': multiply(number1, number2), '/': divide(number1, number2)}
action = (input('+,-,*,/'))
print(choose_action[action])

# Task 11

data = []


def check_db(func):
    def wrapper(*args):
        if data:
            func(*args)
        else:
            print('data is empty')
    return wrapper


@check_db
def look():
    print(data)


look()
data.append(3)
look()

# Task 12


def check_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print('error')
    return wrapper


@check_error
def wrong():
    pirnt('hello')


wrong()

#Task 13

product_list = {}


def check(func):
    def wrapper(*args):
        if product_list:
            func(*args)
        else:
            quit('your list is empty')
    return wrapper

def choice(func):
    def wrapper():
        choice = int(input('Введите номер: ')) - 1
        try:
            func(choice)
        except:
            print('Нет такого товара')
    return wrapper

def create_product():
    product = {'name': input('enter name: '),
               'quantity': input('enter quantity: '),
               'price': input('enter price: ')}
    product_list.setdefault(product['name'], product)


@check
def look_products():
    for number, value in enumerate(product_list.values(), 1):
        print(f"{number} Товар - {value['name']},"
              f" количество {value['quantity']},"
              f" цена - {value['price']}")





@check
@choice
def look_product(num=0):
    product = list(product_list.values())[num]
    print(f" Товар - {product['name']},"
          f" количество {product['quantity']},"
          f" цена - {product['price']}")

@check
@choice
def update_product(num=0):
    product = list(product_list.values())[num]
    product.update({'name': input('Enter new name: '),
                    'quantity': input('Enter new quantity: '),
                    'price': input('Enter new price: ')})

@check
@choice
def delete_product(num=0):
    del product_list[list(product_list.values())[num]['name']]


def menu():
    while True:
        act = input('1 - create,2-look all,3-look one,4-update,5-delete,6-exit: ')
        if act == '1':
            create_product()
        if act == '2':
            look_products()
        if act == '3':
            look_product()
        if act == '4':
            update_product()
        if act == '5':
            delete_product()
        if act == '6':
            break


menu()

# Task 1

weight = float(input('Enter your weight (kg)'))
height = float(input('Enter your height(m)'))
imt = weight / height ** 2
if imt <= 18.5:
    print('У вас анорексия')
elif 18.5 < imt <= 30:
    print('У вас нормальное состояние здоровья')
else:
    print('У вас ожирение')

# Task 2

nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
print(nat.replace('Fast', 'Gigabit'))

# Task 3

name = input('Enter your name')
prof = input('Enter your profession')
exp = input('Enter your experience')
print(f'Ваше имя -  {name} \nВаша профессия -  {prof} \nВаш стаж -  {exp}')

# Task 4

num1 = int(input('Enter first number: '))
action = input('Enter action(+,-,* or /: ')
num2 = int(input('Enter second number: '))
if action == '+':
    result = num1 + num2
    print(result)
elif action == '-':
    result = num1 - num2
    print(result)
elif action == '*':
    result = num1 * num2
    print(result)
elif action == '/':
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print('На ноль делить нельзя')
else:
    print('Не корректное действие')

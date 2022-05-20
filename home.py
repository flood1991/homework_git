def round_standart(num):
    if num >= 0:
        num = round(num + 0.5, 0)
    else:
        num = round(num - 0.5, 0)
    return int(num)


print(round_standart(-2.5))
x = 0.1 + 0.2
print(x)


def eqv(a, b, c):
    res = a+b
    if a > b:
        return abs(c - res) <= 0.0001 * abs(a)
    else:
        return abs(c - res) <= 0.0001 * abs(b)


print(eqv(0.12, 0.31, 0.43))
print(eqv(-0.12, -0.31, -0.43))
print(eqv(0.1, 0.2, 0.4))
print(eqv(0.1, 0.2, 0.3))


def help_bool(letter=None):
    if letter == 'k' or letter == 'к':
        return 'Коммутативность \n A or B = B or A \n A and B = B and A'
    elif letter == 'д':
        return 'Дистрибутивность \n A and (B or C) == (A and B) or (A and C) \nA or (B and C) == (A or B) and (A or C)'
    elif letter == 'a' or letter == 'а':
        return 'Ассоциативность \n A or (B or C) == (A or B) or C == A or B or C\n' \
               'A and (B and C) == (A and B) and C == A and B and C'
    elif letter == 'м':
        return 'Теорема де Моргана \n not (A or B) == not A and not B\n'\
              'not (A and B) == not A or not B\n'\
              'not(not(A)) = A\n'\
              'not (A < B) == A >= B'
    else:
        return 'к - Коммутативность\n'\
              'д - Дистрибутивность\n'\
              'а - Ассоциативность\n'\
              'м - Теорема де Моргана'


print(help_bool('к'))
print(help_bool(22))
print(help_bool())
print(not 7 and 3 or 5)


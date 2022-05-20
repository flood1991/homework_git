def capitalize(word):
    new_word = ''
    for i in word.split():
        new_word += (i.replace(i[0], chr(ord(i[0])-32), 1))+' '
        print(i)
    return ''.join(new_word)
print(capitalize('i wanna tastte you but your lips are venomous poison'))


def expt(b, n):
    if n == 0:
        return 1
    return b*expt(b, n-1)
print(expt(2,3))
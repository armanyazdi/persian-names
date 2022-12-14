import os
from random import randrange


def fullname_en(sex='r'):
    if sex == 'male' or sex == 'm':
        sex = 0
    elif sex == 'female' or sex == 'f':
        sex = 1
    elif sex == 'random' or sex == 'r':
        sex = randrange(2)
    else:
        return None

    path = os.path.dirname(__file__)
    file = ['male_en.txt', 'female_en.txt']
    sfx1 = [
        '', '', '', '', '', '', '', '', '', '', '',
        'pour',
        'zadeh',
        'far',
        'fard',
        'an',
        'kia',
        'rad',
        'zand',
        'khah',
        'nia',
        'mehr'
    ]
    sfx2 = [
        'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i',
        'pour',
        'zadeh',
        'far',
        'fard',
        'khani',
        'vand',
        'lou',
        'nia'
    ]

    def first(sex):
        f = open(path + '/data/' + file[sex], 'r', encoding='utf8')
        names = f.read().split('\n')
        first = names[randrange(len(names))]
        return first

    def last():
        f = open(path + '/data/' + file[0], 'r', encoding='utf8')
        names = f.read().split('\n')
        last = names[randrange(len(names))]
        if last[1:] == 'ostafa' or last[1:] == 'ousa' or last[1:] == 'ahya':
            last += 'vi'
        elif last[1:] == 'orteza':
            last = last.replace('ez', 'az') + 'vi'
        elif last[1:] == 'hosro':
            last = last.replace('ro', 'ravi')
        elif last[-1] == 'a' or last[-1] == 'o' or last[-1] == 'u':
            last += 'ei'
        elif last[-1] == 'i':
            pass
        else:
            last += ['i', ''][randrange(2)]
        if len(last) > 10 and last[-1] == 'i':
            last += ''
        elif len(last) > 10 and last[-1] != 'i':
            last += 'i'
        elif last[-1] == 'i':
            last += sfx1[randrange(len(sfx1))]
        else:
            last += sfx2[randrange(len(sfx2))]
        return last

    return first(sex) + ' ' + last()


def fullname_fa(sex='r'):
    if sex == 'male' or sex == 'm':
        sex = 0
    elif sex == 'female' or sex == 'f':
        sex = 1
    elif sex == 'random' or sex == 'r':
        sex = randrange(2)
    else:
        return None

    path = os.path.dirname(__file__)
    file = ['male_fa.txt', 'female_fa.txt']
    sfx1 = [
        '', '', '', '', '', '', '', '', '', '', '',
        ' ??????',
        ' ????????',
        ' ????',
        ' ??????',
        '????',
        ' ??????',
        ' ??????',
        ' ??????',
        ' ????????',
        ' ??????',
        ' ??????'
    ]
    sfx2 = [
        '??', '??', '??', '??', '??', '??', '??', '??',
        ' ??????',
        ' ????????',
        ' ????',
        ' ??????',
        ' ????????',
        ' ??????',
        ' ????',
        ' ??????'
    ]

    def first(sex):
        f = open(path + '/data/' + file[sex], 'r', encoding='utf8')
        names = f.read().split('\n')
        first = names[randrange(len(names))]
        return first

    def last():
        f = open(path + '/data/' + file[0], 'r', encoding='utf8')
        names = f.read().split('\n')
        last = names[randrange(len(names))]
        if last == '??????????' or last == '??????????' or last == '????????':
            last = last.replace('??', '????')
        elif last == '????????':
            last = last.replace('????', '??????')
        elif last == '????????':
            pass
        elif last[-1] == '??' or last[-1] == '??':
            last += '????'
        elif last[-1] == '??':
            pass
        else:
            last += ['??', ''][randrange(2)]
        if last[-1] == '??':
            last += sfx1[randrange(len(sfx1))]
        else:
            last += sfx2[randrange(len(sfx2))]
        return last

    return first(sex) + ' ' + last()

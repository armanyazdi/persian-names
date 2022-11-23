import os
from random import randrange


def fullname_en(sex):
    if sex == 'male' or sex == 'm':
        sex = 0
    elif sex == 'female' or sex == 'f':
        sex = 1
    elif sex == 'random' or sex == 'r':
        sex = randrange(2)
    else:
        return None

    path = os.path.dirname(__file__)
    file = ['/data/male.txt', '/data/female.txt']
    isfx = ['', '', '', '', '', '', '', '', '', 'pour', 'zadeh', 'far', 'fard', 'an', 'kia', 'rad', 'zand', 'khah']
    nsfx = ['i', 'i', 'i', 'i', 'i', 'i', 'i', 'pour', 'zadeh', 'far', 'fard', 'khani', 'vand', 'lou']

    def first(sex):
        f = open(path + file[sex], 'r')
        names = f.read().split('\n')
        first = names[randrange(len(names))]
        return first

    def last():
        f = open(path + file[0], 'r')
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
            last += isfx[randrange(len(isfx))]
        else:
            last += nsfx[randrange(len(nsfx))]
        return last

    return first(sex) + ' ' + last()


def fullname_fa(sex):
    if sex == 'male' or sex == 'm':
        sex = 0
    elif sex == 'female' or sex == 'f':
        sex = 1
    elif sex == 'random' or sex == 'r':
        sex = randrange(2)
    else:
        return None

    path = os.path.dirname(__file__)
    file = ['/data/male_fa.txt', '/data/female_fa.txt']
    isfx = ['', '', '', '', '', '', '', '', '', ' پور', ' زاده', ' فر', ' فرد', 'ان', ' کیا', ' راد', ' زند', ' خواه']
    nsfx = ['ی', 'ی', 'ی', 'ی', 'ی', 'ی', 'ی', ' پور', ' زاده', ' فر', ' فرد', ' خانی', ' وند', ' لو']

    def first(sex):
        f = open(path + file[sex], 'r')
        names = f.read().split('\n')
        first = names[randrange(len(names))]
        return first

    def last():
        f = open(path + file[0], 'r')
        names = f.read().split('\n')
        last = names[randrange(len(names))]
        if last == 'مرتضی' or last == 'مصطفی' or last == 'موسی':
            last = last.replace('ی', 'وی')
        elif last == 'یحیی':
            last = last.replace('یی', 'یوی')
        elif last == 'خسرو':
            pass
        elif last[-1] == 'ا' or last[-1] == 'و':
            last += 'ئی'
        elif last[-1] == 'ی':
            pass
        else:
            last += ['ی', ''][randrange(2)]
        if last[-1] == 'ی':
            last += isfx[randrange(len(isfx))]
        else:
            last += nsfx[randrange(len(nsfx))]
        return last

    return first(sex) + ' ' + last()

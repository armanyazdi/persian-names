import os
from random import randrange

path = os.path.dirname(__file__)


def fullname_en(sex='r'):
    sex = sex.lower()

    if sex == 'male' or sex == 'm':
        sex = 0
    elif sex == 'female' or sex == 'f':
        sex = 1
    elif sex == 'random' or sex == 'r':
        sex = randrange(2)
    else:
        return None

    files = ['male_en.txt', 'female_en.txt']
    some_suffixes = [
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
    more_suffixes = [
        'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i',
        'pour',
        'zadeh',
        'far',
        'fard',
        'khani',
        'vand',
        'lou',
        'nia',
        'zehi'
    ]

    def firstname():
        f = open(path + '/data/' + files[sex], 'r', encoding='utf8')
        names = f.read().split('\n')
        f.close()
        first_name = names[randrange(len(names))]
        return first_name

    def lastname():
        f = open(path + '/data/' + files[0], 'r', encoding='utf8')
        names = f.read().split('\n')
        f.close()
        last_name = names[randrange(len(names))]
        if last_name[1:] == 'ostafa' or last_name[1:] == 'ousa' or last_name[1:] == 'ahya':
            last_name += 'vi'
        elif last_name[1:] == 'orteza':
            last_name = last_name.replace('ez', 'az') + 'vi'
        elif last_name[1:] == 'hosro':
            last_name = last_name.replace('ro', 'ravi')
        elif last_name[-1] == 'a' or last_name[-1] == 'o' or last_name[-1] == 'u':
            last_name += 'ei'
        elif last_name[-1] == 'i':
            pass
        else:
            last_name += ['i', ''][randrange(2)]
        if len(last_name) > 10 and last_name[-1] == 'i':
            last_name += ''
        elif len(last_name) > 10 and last_name[-1] != 'i':
            last_name += 'i'
        elif last_name[-1] == 'i':
            last_name += some_suffixes[randrange(len(some_suffixes))]
        else:
            last_name += more_suffixes[randrange(len(more_suffixes))]
        return last_name

    return firstname() + ' ' + lastname()


def fullname_fa(sex='r'):
    sex = sex.lower()

    if sex == 'male' or sex == 'm':
        sex = 0
    elif sex == 'female' or sex == 'f':
        sex = 1
    elif sex == 'random' or sex == 'r':
        sex = randrange(2)
    else:
        return None

    files = ['male_fa.txt', 'female_fa.txt']
    some_suffixes = [
        '', '', '', '', '', '', '', '', '', '', '',
        ' پور',
        ' زاده',
        ' فر',
        ' فرد',
        'ان',
        ' کیا',
        ' راد',
        ' زند',
        ' خواه',
        ' نیا',
        ' مهر'
    ]
    more_suffixes = [
        'ی', 'ی', 'ی', 'ی', 'ی', 'ی', 'ی', 'ی', 'ی',
        ' پور',
        ' زاده',
        ' فر',
        ' فرد',
        ' خانی',
        ' وند',
        ' لو',
        ' نیا',
        ' زهی'
    ]

    def firstname():
        f = open(path + '/data/' + files[sex], 'r', encoding='utf8')
        names = f.read().split('\n')
        f.close()
        first_name = names[randrange(len(names))]
        return first_name

    def lastname():
        f = open(path + '/data/' + files[0], 'r', encoding='utf8')
        names = f.read().split('\n')
        f.close()
        last_name = names[randrange(len(names))]
        if last_name == 'مرتضی' or last_name == 'مصطفی' or last_name == 'موسی':
            last_name = last_name.replace('ی', 'وی')
        elif last_name == 'یحیی':
            last_name = last_name.replace('یی', 'یوی')
        elif last_name == 'خسرو':
            pass
        elif last_name[-1] == 'ا' or last_name[-1] == 'و':
            last_name += 'ئی'
        elif last_name[-1] == 'ی':
            pass
        else:
            last_name += ['ی', ''][randrange(2)]
        if last_name[-1] == 'ی':
            last_name += some_suffixes[randrange(len(some_suffixes))]
        else:
            last_name += more_suffixes[randrange(len(more_suffixes))]
        return last_name

    return firstname() + ' ' + lastname()

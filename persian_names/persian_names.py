import os
from random import randrange, randint

path = os.path.dirname(__file__)
files = ['male_en.txt', 'female_en.txt', 'male_fa.txt', 'female_fa.txt']


def firstname_en(sex='r'):
    sex = sex.lower()

    if sex == 'male' or sex == 'm':
        sex = 0
    elif sex == 'female' or sex == 'f':
        sex = 1
    elif sex == 'random' or sex == 'r':
        sex = randrange(2)
    else:
        return None

    f = open(path + '/data/' + files[sex], 'r', encoding='utf8')
    names = f.read().split('\n')
    f.close()
    first_name = names[randrange(len(names))]

    return first_name


def lastname_en():
    # English Prefixes and Suffixes
    some_prefixes = [
        'Mir',
        'Agha',
        'Abou',
        'Pour',
        'Nour',
        'Nasr',
        'Zand',
        'Seyed',
        'Amir',
        'Aziz',
        'Shah',
        'Nik',
        'Haj',
        'Haji',
        'Soufi',
        'Sheikh',
        'Mirza',
        'Ostad',
        'Malek',
        'Khan',
        'Beig',
        'Arab'
    ]
    some_suffixes = [
        'pour', '',
        'zadeh', '',
        'far', '',
        'fard', '',
        'an', '',
        'kia', '',
        'rad', '',
        'zand', '',
        'khah', '',
        'nia', '',
        'mehr', '',
        'azar', '',
        'sadr', '',
        'kohan', '',
        'nejad', '',
        'bayat', '',
        'yekta' '',
        'sabet' '',
        'azad', '',
        'zare', '',
        'moghaddam', '',
    ]
    more_suffixes = [
        'pour', 'i',
        'zadeh', 'i',
        'far', 'i',
        'fard', 'i',
        'khani', 'i',
        'vand', 'i',
        'lou', 'i',
        'nia', 'i',
        'zehi', 'i',
        'nejad', 'i',
        'beigi', 'i',
        'zare', 'i',
    ]
    arabic_names = []
    illegal_names = []

    f = open(path + '/data/' + files[0], 'r', encoding='utf8')
    names = f.read().split('\n')
    f.close()
    last_name = names[randrange(len(names))]

    for i in names[:26]:
        arabic_names.append(i)

    for i in names[26:50]:
        illegal_names.append(i)

    while last_name in illegal_names:
        last_name = names[randrange(len(names))]

    if last_name == 'Mostafa' or last_name == 'Mousa' or last_name == 'Yahya' or last_name == 'Kasra' or last_name == 'Mojtaba':
        last_name += 'vi'
    elif last_name == 'Morteza':
        last_name = last_name.replace('ez', 'az') + 'vi'
    elif last_name == 'Ali' or last_name == 'Mahdi':
        last_name = last_name.replace('i', ['i', 'avi'][randrange(2)])
    elif last_name == 'Khosro':
        last_name = last_name.replace('ro', 'ravi')
    elif last_name[-1] == 'a' or last_name[-1] == 'o' or last_name[-1] == 'u':
        last_name += 'ei'
    elif last_name[-1] == 'i':
        pass
    else:
        last_name += ['i', ''][randrange(2)]

    if last_name[:-1] in arabic_names or last_name[:-2] in arabic_names:
        prefix = some_prefixes[randrange(len(some_prefixes))]
        suffix = some_suffixes[randrange(len(some_suffixes))]

        if suffix == '' and prefix != '' and prefix[-1] == last_name[0].lower():
            last_name = prefix + ' ' + last_name
        elif suffix == '':
            last_name = prefix + last_name.lower()
        else:
            last_name += suffix
    elif (len(last_name) <= 5 and last_name[-1] == 'i') or last_name.lower().endswith('ali') or last_name.lower().endswith('mahdi'):
        last_name += ['pour', 'zadeh', 'far', 'fard', 'an', 'kia', 'khani', 'vand', 'nia', 'nejad', 'beigi'][randrange(11)]
    elif len(last_name) > 10 and last_name[-1] == 'i':
        last_name += ''
    elif len(last_name) > 10 and last_name[-1] != 'i':
        last_name += 'i'
    elif last_name[-1] == 'i':
        last_name += some_suffixes[randrange(len(some_suffixes))]
    else:
        last_name += more_suffixes[randrange(len(more_suffixes))]

    return last_name


def fullname_en(sex='r'):
    return firstname_en(sex) + ' ' + lastname_en()


def firstname_fa(sex='r'):
    sex = sex.lower()

    if sex == 'male' or sex == 'm':
        sex = 2
    elif sex == 'female' or sex == 'f':
        sex = 3
    elif sex == 'random' or sex == 'r':
        sex = randint(2, 3)
    else:
        return None

    f = open(path + '/data/' + files[sex], 'r', encoding='utf8')
    names = f.read().split('\n')
    f.close()
    first_name = names[randrange(len(names))]

    return first_name


def lastname_fa():
    # Farsi Prefixes and Suffixes
    some_prefixes = [
        'میر',
        'آقا',
        'ابو',
        'پور',
        'نور',
        'نصر',
        'زند',
        'سید',
        'امیر',
        'عزیز',
        'شاه ',
        'نیک ',
        'حاج ',
        'حاجی ',
        'صوفی ',
        'شیخ ',
        'میرزا ',
        'استاد ',
        'ملک ',
        'خان ',
        'بیگ ',
        'عرب '
    ]
    some_suffixes = [
        ' پور', '',
        ' زاده', '',
        ' فر', '',
        ' فرد', '',
        'ان', '',
        ' کیا', '',
        ' راد', '',
        ' زند', '',
        ' خواه', '',
        ' نیا', '',
        ' مهر', '',
        ' آذر', '',
        ' صدر', '',
        ' کهن', '',
        ' نژاد', '',
        ' بیات', '',
        ' یکتا', '',
        ' ثابت', '',
        ' آزاد', '',
        ' زارع', '',
        ' مقدم', '',
    ]
    more_suffixes = [
        ' پور', 'ی',
        ' زاده', 'ی',
        ' فر', 'ی',
        ' فرد', 'ی',
        ' خانی', 'ی',
        ' وند', 'ی',
        ' لو', 'ی',
        ' نیا', 'ی',
        ' زهی', 'ی',
        ' نژاد', 'ی',
        ' بیگی', 'ی',
        ' زارع', 'ی',
    ]
    arabic_names = []
    illegal_names = []

    f = open(path + '/data/' + files[2], 'r', encoding='utf8')
    names = f.read().split('\n')
    f.close()
    last_name = names[randrange(len(names))]

    for i in names[:26]:
        arabic_names.append(i)

    for i in names[26:50]:
        illegal_names.append(i)

    while last_name in illegal_names:
        last_name = names[randrange(len(names))]

    if last_name == 'مرتضی' or last_name == 'مصطفی' or last_name == 'موسی' or last_name == 'کسری' or last_name == 'مجتبی':
        last_name = last_name.replace('ی', 'وی')
    elif last_name == 'یحیی':
        last_name = last_name.replace('یی', 'یوی')
    elif last_name == 'علی' or last_name == 'مهدی':
        last_name = last_name.replace('ی', ['ی', 'وی'][randrange(2)])
    elif last_name == 'خسرو':
        pass
    elif last_name[-1] == 'ا' or last_name[-1] == 'و':
        last_name += 'یی'
    elif last_name[-1] == 'ی':
        pass
    else:
        last_name += ['ی', ''][randrange(2)]

    if last_name[:-1] in arabic_names or last_name[:-2] in arabic_names:
        prefix = some_prefixes[randrange(len(some_prefixes))]
        suffix = some_suffixes[randrange(len(some_suffixes))]

        if suffix == '':
            last_name = prefix + last_name
        else:
            last_name += suffix
    elif (len(last_name) <= 4 and last_name[-1] == 'ی') or last_name.endswith('علی') or last_name.endswith('مهدی'):
        last_name += [' پور', ' زاده', ' فر', ' فرد', 'ان', ' کیا', ' خانی', ' وند', ' نیا', ' نژاد', ' بیگی'][randrange(11)]
    elif last_name[-1] == 'ی':
        last_name += some_suffixes[randrange(len(some_suffixes))]
    else:
        last_name += more_suffixes[randrange(len(more_suffixes))]

    return last_name


def fullname_fa(sex='r'):
    return firstname_fa(sex) + ' ' + lastname_fa()

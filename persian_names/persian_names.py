import os
from random import randrange, choice

# Define the path to the directory containing the data files
path = os.path.dirname(__file__)
files = ['male_en.txt', 'female_en.txt', 'male_fa.txt', 'female_fa.txt', 'region_en.txt', 'region_fa.txt']


# Preload names from files into lists
def load_names(filename):
    with open(os.path.join(path, 'data', filename), 'r', encoding='utf8') as f:
        return f.read().splitlines()


# Load names from the corresponding files
male_names_en = load_names(files[0])
female_names_en = load_names(files[1])
male_names_fa = load_names(files[2])
female_names_fa = load_names(files[3])
regions_en = load_names(files[4])
regions_fa = load_names(files[5])


# Generate a random English first name based on the specified sex
def firstname_en(sex='r'):
    sex = sex.lower()

    # Determine the list of names to use based on the sex parameter
    if sex == 'male' or sex == 'm':
        names = male_names_en
    elif sex == 'female' or sex == 'f':
        names = female_names_en
    elif sex == 'random' or sex == 'r':
        names = choice([male_names_en, female_names_en])
    else:
        return None

    # Return a random name from the selected list
    return choice(names)


# Define English prefixes and suffixes
some_prefixes_en = [
    'Mir',
    'Pir',
    'Yar',
    'Agha',
    'Abou',
    'Pour',
    'Nour',
    'Nasr',
    'Zand',
    'Seyed',
    'Amir',
    'Aziz',
    'Sayad',
    'Zahed',
    'Shah',
    'Nik',
    'Haj',
    'Haji',
    'Soufi',
    'Afzal',
    'Fazel',
    'Sheikh',
    'Mirza',
    'Ostad',
    'Khajeh',
    'Malek',
    'Khan',
    'Beig',
    'Arab',
    'Manesh',
]
some_suffixes_en = [
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
    'roshan', '',
    'tabar', '',
    'rashed', '',
    'dana', '',
    'zadegan', '',
    'manesh', '',
    'yar', '',
]
more_suffixes_en = [
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
    'tabar', 'i',
    'manesh', 'i',
    'pourian', 'i',
]


# Generate a random English last name
def lastname_en():
    # Lists of names to exclude or treat specially
    illegal_names = male_names_en[27:62]
    arabic_names = male_names_en[:27]

    # Select a random last name, ensuring it's not in the illegal list
    last_name = choice(male_names_en)
    while last_name in illegal_names:
        last_name = choice(male_names_en)

    # Modify the last name based on specific rules
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

    # Add a prefix or suffix based on various conditions
    if last_name[:-1] in arabic_names or last_name[:-2] in arabic_names:
        prefix = choice(some_prefixes_en)
        suffix = choice(some_suffixes_en)
        if suffix == '':
            last_name = prefix + last_name.lower()
        else:
            last_name += suffix
    elif (len(last_name) <= 5 and last_name[-1] == 'i') or last_name.lower().endswith(
            'ali') or last_name.lower().endswith('mahdi'):
        last_name += choice(['pour', 'zadeh', 'far', 'fard', 'an', 'kia', 'khani', 'vand', 'nia', 'nejad', 'beigi'])
    elif len(last_name) > 10 and last_name[-1] == 'i':
        last_name += ''
    elif len(last_name) > 10 and last_name[-1] != 'i':
        last_name += 'i'
    elif last_name[-1] == 'i':
        selected_list = choice([some_suffixes_en, regions_en])
        chosen_item = choice(selected_list)
        if selected_list is regions_en:
            last_name = choice([last_name + ' ' + chosen_item + 'i', chosen_item + 'i'])
        else:
            last_name += chosen_item
    else:
        last_name += choice(more_suffixes_en)

    return last_name


# Generate a random English full name
def fullname_en(sex='r'):
    return firstname_en(sex) + ' ' + lastname_en()


# Generate a random Farsi first name based on the specified sex
def firstname_fa(sex='r'):
    sex = sex.lower()

    # Determine the list of names to use based on the sex parameter
    if sex == 'male' or sex == 'm':
        names = male_names_fa
    elif sex == 'female' or sex == 'f':
        names = female_names_fa
    elif sex == 'random' or sex == 'r':
        names = choice([male_names_fa, female_names_fa])
    else:
        return None

    # Return a random name from the selected list
    return choice(names)


# Define Farsi prefixes and suffixes
some_prefixes_fa = [
    'میر',
    'پیر',
    'یار',
    'آقا',
    'ابو',
    'پور',
    'نور',
    'نصر',
    'زند',
    'سید',
    'امیر',
    'عزیز',
    'صیاد',
    'زاهد',
    'شاه ',
    'نیک ',
    'حاج ',
    'حاجی ',
    'صوفی ',
    'افضل ',
    'فاضل ',
    'شیخ ',
    'میرزا ',
    'استاد ',
    'خواجه ',
    'ملک ',
    'خان ',
    'بیگ ',
    'عرب ',
    'منش ',
]
some_suffixes_fa = [
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
    ' روشن', '',
    ' تبار', '',
    ' راشد', '',
    ' دانا', '',
    ' زادگان', '',
    ' منش', '',
    ' یار', '',
]
more_suffixes_fa = [
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
    ' تبار', 'ی',
    ' منش', 'ی',
    ' پوریان', 'ی',
]


# Generate a random Farsi last name
def lastname_fa():
    # Lists of names to exclude or treat specially
    illegal_names = male_names_fa[27:62]
    arabic_names = male_names_fa[:27]

    # Select a random last name, ensuring it's not in the illegal list
    last_name = choice(male_names_fa)
    while last_name in illegal_names:
        last_name = choice(male_names_fa)

    # Modify the last name based on specific rules
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

    # Add a prefix or suffix based on various conditions
    if last_name[:-1] in arabic_names or last_name[:-2] in arabic_names:
        prefix = choice(some_prefixes_fa)
        suffix = choice(some_suffixes_fa)
        if suffix == '':
            last_name = prefix + last_name
        else:
            last_name += suffix
    elif (len(last_name) <= 4 and last_name[-1] == 'ی') or last_name.endswith('علی') or last_name.endswith('مهدی'):
        last_name += choice([' پور', ' زاده', ' فر', ' فرد', 'ان', ' کیا', ' خانی', ' وند', ' نیا', ' نژاد', ' بیگی'])
    elif last_name[-1] == 'ی':
        selected_list = choice([some_suffixes_fa, regions_fa])
        chosen_item = choice(selected_list)
        if selected_list is regions_fa:
            last_name = choice([last_name + ' ' + chosen_item + 'ی', chosen_item + 'ی'])
        else:
            last_name += chosen_item
    else:
        last_name += choice(more_suffixes_fa)

    return last_name


# Generate a random Farsi full name
def fullname_fa(sex='r'):
    return firstname_fa(sex) + ' ' + lastname_fa()

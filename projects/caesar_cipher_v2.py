# Каждый символ слова сдвигается на длину слова
def enc_or_dec():
    answer = input('Шифрование или дешифрование? (ш/д): ').lower().strip()
    while True:
        if answer in ['ш', 'i']:
            return 'enc'
        elif answer in ['д', 'l']:
            return 'dec'
        else:
            answer = input('ш/д: ').strip()


def language_pack():
    answer = input('Русский или английский? (ru/en): ').lower().strip()
    while True:
        if answer in ['ru', 'кг', 'ру']:
            return 'ru'
        elif answer in ['en', 'ут', 'анг', 'англ']:
            return 'en'
        else:
            answer = input('ru/en: ').strip()


def is_valid_text(text, lang_pack):
    flag = True
    letters = 0
    for c in text.lower():
        if c.isalpha():
            letters += 1
            if c not in lang_pack:
                flag = False
                break
    return all([flag, letters])


def is_valid(language):
    ru_pack = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    en_pack = 'abcdefghijklmnopqrstuvwxyz'
    text = input('Введите текст: ').strip()
    if language == 'ru':
        while True:
            if is_valid_text(text, ru_pack):
                return text
            else:
                text = input('Введите текст на выбранном языке: ').strip()
    if language == 'en':
        while True:
            if is_valid_text(text, en_pack):
                return text
            else:
                text = input('Введите текст на выбранном языке: ').strip()


def enc(text, chr_count, limit):
    text_list = text.split()
    encrypted_text = ''
    for elem in text_list:
        len_elem = len([i for i in elem if i.isalpha()])
        result = ''
        for c in elem:
            if c.isalpha():
                encrypt = ord(c.lower()) + len_elem
                if encrypt > limit:
                    encrypt -= chr_count
                if c.isupper():
                    result += chr(encrypt).upper()
                else:
                    result += chr(encrypt)
            else:
                result += c
        encrypted_text += result + ' '
    return encrypted_text


def dec(text, chr_count, limit):
    text_list = text.split()
    encrypted_text = ''
    for elem in text_list:
        len_elem = len([i for i in elem if i.isalpha()])
        result = ''
        for c in elem:
            if c.isalpha():
                encrypt = ord(c.lower()) - len_elem
                if encrypt < limit:
                    encrypt += chr_count
                if c.isupper():
                    result += chr(encrypt).upper()
                else:
                    result += chr(encrypt)
            else:
                result += c
        encrypted_text += result + ' '
    return encrypted_text


def encryption(text, language):
    if language == 'ru':
        return enc(text, 32, ord('я'))
    if language == 'en':
        return enc(text, 26, ord('z'))


def decryption(text, language):
    if language == 'ru':
        return dec(text, 32, ord('а'))
    if language == 'en':
        return dec(text, 26, ord('a'))


def is_continue():
    answer = input('\nЖелаете повторить? (да/нет): ').strip()
    while True:
        if answer in ['да', 'lf', 'д', 'l']:
            return True
        elif answer in ['нет', 'ytn', 'н', 'y']:
            return False
        else:
            answer = input('да/нет: ').strip()


def caesar_cipher():
    direction = enc_or_dec()
    language = language_pack()
    text = is_valid(language)
    if direction == 'enc':
        return ['\nРезультат:', encryption(text, language)]
    if direction == 'dec':
        return ['\nРезультат:', decryption(text, language)]


while True:
    print(*caesar_cipher(), sep='\n')
    if is_continue():
        print('-' * 30)
        continue
    else:
        print('Всего хорошего!')
        break

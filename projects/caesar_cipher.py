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


def is_valid_lang(text, lang_pack):
    flag = True
    for c in text.lower():
        if c not in lang_pack:
            flag = False
            break
    return flag


def is_valid(language):
    ru_pack = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    en_pack = 'abcdefghijklmnopqrstuvwxyz'
    text = input('Введите текст: ').strip()
    if language == 'ru':
        while True:
            if is_valid_lang(text, ru_pack):
                return text
            else:
                text = input('Введите текст на выбранном языке: ').strip()
    if language == 'en':
        while True:
            if is_valid_lang(text, en_pack):
                return text
            else:
                text = input('Введите текст на выбранном языке: ').strip()


def valid_step():
    step = input('Введите шаг сдвига: ').strip()
    while True:
        if step.isdigit() and int(step) > 0:
            return int(step)
        else:
            step = input('Введите число > 0: ').strip()


def is_step():
    answer = input('Известен ли шаг сдвига? (д/н): ').lower().strip()
    while True:
        if answer in ['д', 'l', 'да', 'lf']:
            step = valid_step()
            return step
        if answer in ['н', 'y', 'нет', 'ytn']:
            return False
        else:
            answer = input('(д/н): ').strip()


def enc(right, chr_count, text, step):
    result = ''
    for c in text:
        if c.isalpha():
            encrypt = ord(c.lower()) + step
            if encrypt > right:
                encrypt -= chr_count
            if c.isupper():
                result += chr(encrypt).upper()
            else:
                result += chr(encrypt)
        else:
            result += c
    return result


def encryption(language, step, text):
    if language == 'ru':
        return enc(ord('я'), 32, text, step)
    if language == 'en':
        return enc(ord('z'), 26, text, step)


def dec(left, chr_count, text, step):
    dictionary = []
    if step:
        result = ''
        for c in text:
            if c.isalpha():
                encrypt = ord(c.lower()) - step
                if encrypt < left:
                    encrypt += chr_count
                if c.isupper():
                    result += chr(encrypt).upper()
                else:
                    result += chr(encrypt)
            else:
                result += c
        return result
    else:
        dec_list = []
        for i in range(1, chr_count):
            result = ''
            for c in text:
                if c.isalpha():
                    encrypt = ord(c.lower()) - i
                    if encrypt < left:
                        encrypt += chr_count
                    if c.isupper():
                        result += chr(encrypt).upper()
                    else:
                        result += chr(encrypt)
                else:
                    result += c
            dec_list.append(result)
        return dec_list


def decryption(language, step, text):
    if language == 'ru':
        return dec(ord('а'), 32, text, step)
    if language == 'en':
        return dec(ord('a'), 26, text, step)


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
        step = valid_step()
        return ['\nРезультат:', encryption(language, step, text)]
    if direction == 'dec':
        step = is_step()
        return ['\nРезультат:', *decryption(language, step, text)]


while True:
    print(*caesar_cipher(), sep='\n')
    if is_continue():
        print('-' * 30)
        continue
    else:
        print('Всего хорошего!')
        break

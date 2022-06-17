import random


def is_valid_num(text):
    num = input(text)
    while True:
        if num.isdigit():
            return int(num)
        else:
            num = input('Введите число: ')


def is_valid_question(text, content):
    question = input(text).lower()
    while True:
        if question == 'y':
            return content
        elif question == 'n':
            return ''
        else:
            question = input('y/n: ')


def is_exc_on(text, chars):
    question = input(text).lower()
    while True:
        if question in ['y', 'n']:
            if question == 'y':
                for c in 'il1Lo0O':
                    chars = chars.replace(c, '')
                return chars
            else:
                return chars
        else:
            question = input('y/n: ')


def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password


def password_generator():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''

    count_of_passwords = is_valid_num('Введите количество паролей: ')
    len_of_password = is_valid_num('Введите длину одного пароля: ')
    digits_on = is_valid_question('Включать ли цифры 0123456789? (y/n): ', digits)
    uppercase_on = is_valid_question('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ',
                                     uppercase_letters)
    lowercase_on = is_valid_question('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n): ',
                                     lowercase_letters)
    symbols_on = is_valid_question('Включать ли символы !#$%&*+-=?@^_? (y/n): ', punctuation)

    chars += digits_on + uppercase_on + lowercase_on + symbols_on
    chars = is_exc_on('Исключать ли неоднозначные символы il1Lo0O? (y/n): ', chars)

    for _ in range(count_of_passwords):
        print(generate_password(len_of_password, chars))


password_generator()

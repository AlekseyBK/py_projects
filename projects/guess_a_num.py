from random import randint


def is_valid_border(right):
    return right.isdigit() and int(right) > 2


def is_valid_num(num, right):
    return num.isdigit() and 1 <= int(num) <= right


def game():
    print('Добро пожаловать в числовую угадайку!')
    while True:
        right = input('\nВведите правую границу диапазона: ')
        while True:
            if is_valid_border(right):
                right = int(right)
                break
            else:
                right = input('Введите число > 2: ')
        rand_num = randint(1, right)
        print('Вводите числа до тех пор, пока не угадаете число:')
        while True:
            num = input()
            while True:
                if is_valid_num(num, right):
                    num = int(num)
                    break
                else:
                    num = input(f'Введите число в диапазоне от 1 до {right}:\n')
            if num < rand_num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif num > rand_num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                break
        while True:
            ans = input('Желаете продолжить? (Y/N) ').lower()
            if ans in ['y', 'n']:
                break
            else:
                ans = input('Y or N: ')
        if ans == 'y':
            continue
        elif ans == 'n':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break


game()

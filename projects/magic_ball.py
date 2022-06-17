import random


def answer():
    answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
               "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
               "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
               "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
    return random.choice(answers)


def magic_ball():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    name = input('Пожалуйста, представьтесь: ')
    print(f'\nПривет, {name}')

    while True:
        question = input('Задай вопрос: ')
        if question.strip() != '':
            print(answer())
        else:
            continue
        question = input('\nХочешь задать еще один вопрос? да/нет: ')
        while True:
            if question not in ['да', 'нет']:
                question = input('да/нет: ')
            else:
                break
        if question == 'да':
            continue
        else:
            print('Возвращайся, если возникнут вопросы')
            break


magic_ball()

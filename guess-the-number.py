# coding: utf8
import random


def guess_random_number():
    ai_number = random.randint(1, 10)
    user_number = int(input('Потрясающий Искуственный Интеллект загадал число от 1 до 10, угадай мои мысли.\n'))
    count = 1
    while ai_number != user_number:
        if ai_number == user_number:
            break
        if user_number < ai_number:
            count += 1
            user_number = int(input('Маловато будет, ещё раз.\n'))
        else:
            count += 1
            user_number = int(input('Перебор, лол, не угадал.\n'))
    print(f'Бинго, это число {ai_number}')
    return print('Быстро ты!') if count < 3\
        else print('Такой из тебя отгадыватель, средненький') if 2 < count <= 5\
        else print('Ну ты и черепаха конечно')


if __name__ == '__main__':
    guess_random_number()

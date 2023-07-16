from random import randint

def check_random_guess(func):
    def wraper(answer, attempts):
        if not answer in range(1, 100):
            answer = randint(1, 100)
        if not attempts in range(1, 10):
            attempts = randint(1, 10)
        func(answer, attempts)
    return wraper


@check_random_guess
def guess(answer, attempts):
    for _ in range(attempts):
        data = int(input('Введите число: '))
        if data == answer:
            print('Число угадано!')
            return
        elif data < answer:
            print('Больше!')
        else:
            print('Меньше!')
    print('Вы проиграли!')


if __name__ == '__main__':
    guess(300, 50)

from random import randint

def count(num: int = 1):
    def deco(func):
        def wraper(answer, attempts):
            for _ in range(num):
                if not answer in range(1, 100):
                    answer = randint(1, 100)
                if not attempts in range(1, 10):
                    attempts = randint(1, 10)
                func(answer, attempts)       
        return wraper
    return deco


@count(3)
def guess(answer, attempts):
    for _ in range(attempts):
        data = int(input('Введите число: '))
        if data == answer:
            print('Число угадано!')
            return True
        elif data < answer:
            print('Больше!')
        else:
            print('Меньше!')
    print('Вы проиграли!')
    return False


if __name__ == '__main__':
    guess(300, 50)
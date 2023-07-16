from random import randint
import json


def count(num: int = 1):
    def deco(func):
        def wraper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)       
        return wraper
    return deco


def check_random_guess(func):
    def wraper(answer, attempts):
        if not answer in range(1, 100):
            answer = randint(1, 100)
        if not attempts in range(1, 10):
            attempts = randint(1, 10)
        func(answer, attempts)
    return wraper


def save_func_to_json(func):
    def wraper(*args, **kwargs):
        data = []
        file_name = func.__name__ + '.json'
        result = func(*args, **kwargs)
        data.append({'args' : args, 'kwargs': kwargs, 'result': result})
        with open(file_name, 'a') as data_input:
            json.dump(data, data_input, indent= 4)        
    return wraper


@count(3)
@check_random_guess
@save_func_to_json
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
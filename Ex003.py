from random import randint
import json

def save_func_to_json(func):
    def wraper(*args, **kwargs):
        data = []
        file_name = func.__name__ + '.json'
        result = func(*args, **kwargs)
        data.append({'args' : args, 'kwargs': kwargs, 'result': result})
        with open(file_name, 'a') as data_input:
            json.dump(data, data_input, indent= 4)        
    return wraper


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
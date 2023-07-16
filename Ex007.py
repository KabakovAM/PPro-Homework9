import math
import cmath
from random import randint
import csv
import json


def from_csv(func):
    def wraper():
        with open ('root.csv', 'r', encoding= 'utf-8') as data_output:
            output = csv.reader(data_output, lineterminator='\n', delimiter=';')
            for line in output:
                func(int(line[0]), int(line[1]), int(line[2]))
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


def create_variables():
    data = []
    count = randint(100, 1000)
    for _ in range(count):
        a = randint(1, 100)
        b = randint(1, 100)
        c = randint(1, 100)
        data.append((a, b, c))
    with open ('root.csv', 'w', encoding= 'utf-8') as data_input:
        input = csv.writer(data_input, lineterminator='\n', delimiter=';')
        input.writerows(data)


@from_csv
@save_func_to_json
def find_roots(a, b, c):
    dis = b ** 2 - 4 * a * c
    if dis > 0:
        x1 = (-b + math.sqrt(dis)) / (2 * a)
        x2 = (-b - math.sqrt(dis)) / (2 * a)
        result = (f'x1 = {x1}x2 = {x2}')
    elif dis == 0:
        x = -b / (2 * a)
        result = (f'x = {x}')
    else:
        x1 = (-b + cmath.sqrt(dis)) / (2 * a)
        x2 = (-b - cmath.sqrt(dis)) / (2 * a)
        result = (f'x1 = {x1}x2 = {x2}')
    return result


if __name__ == '__main__':
    create_variables()
    find_roots()
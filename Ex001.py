def guess(answer, attempts):
    def guessing_game():
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
    return guessing_game


if __name__ == '__main__':
    game = guess(50, 10)
    game()
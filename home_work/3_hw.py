import day as day


def max_number(a, b):
    if a > b:
        print(a)
    else:
        print(b)

max_number(a = 156, b = 200)

def diff_number(a, b):
    if a + 135 == b or a - 135 == b:
        print('Yes')
    else:
        print('No')

diff_number(a = 0, b = 136)

def season(a):
    if a == 12 or a == 1 or a == 2:
        print('Зима')
    elif a >= 3 and a <= 5:
        print('Весна')
    elif a >= 6 and a <= 8:
        print('Лето')
    elif a >= 9 and a <= 11:
        print('Осень')
    else:
        print('Введите число от 1 до 12')

season(11)

def diff_number1(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')

diff_number1(10, 10, 10)

def list(a, b, c, d, e):
    if a > 0 or b > 0 or c > 0 or d > 0 or e > 0:
        print('Количество положительных чисел = ', (a > 0) + (b > 0) + (c > 0) + (d > 0) + (e > 0))
    else:
        print('Количество положительных чисел = ')

list(a = 1, b = 2, c = 3, d = 5, e = -10)

def day(year, month):
    if year >= 1 and month >= 1:
        print(day == (year*12*29) + (month*29))
    else:
        print('Введите корректное число')

day(year = 1, month = 2)

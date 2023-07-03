num = 0

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

str_1 = 'no'
str_2 = 'test1'

if str_1 in str_2:
    print('ДА')
else:
    print('НЕТ')

num_float = 3.14

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

year = 1
def student_rank(year):
    if year >= 1 and year <= 4:
        print('Бакалавр')
    elif year >= 5 and year <= 6:
        print('Магистр')
    elif year >= 7 and year <= 9:
        print('Аспирант')
    else:
        print('Введите корректный год обучения')

student_rank(809)

number = 10
def number(sign):
    if sign > 100 or sign < -100:
        print('-')
    else:
        print('+')

number(7)

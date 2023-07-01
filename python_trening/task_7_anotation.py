a: int = 5
b: str = 'строка'
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return "" * (max(0, width - len(s))) + s

print(indent('123', 123))

def string_length(s: str = '') -> int:
    return len(s)

print(string_length())

a: list = [10, 15, 25]
b: list = [1995, 2000, 2020, 2023]

def min_list(a: list, b: list) -> int:
    return max(len(a), len(b))

print(min_list(a, b))

def append_list(my_list: list):
    my_list.append('test')
    return my_list

print(append_list(['один', 2, 3]))

def sum_list(my_list: list) -> int:
    result = 0
    for elem in my_list:
        result = result + elem
    return result

print(sum_list([1, 2, 3]))

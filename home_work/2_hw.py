a: int = 1
b: float = 3.14
c: str = "Hi"
d: list = [1, 2, 3]
e: bool = 10 > 9
def task_1(a: int, b: float, c: str, d: list, e: bool):
    return a, b, c, d, e

print(task_1(a, b, c, d, e))

def task_2(a = [1, 2, 3, 5, 8, 13, 21]):
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]

print(task_2())

def task_3(a, b):
    # a = 6
    # b = 2
    return a ** b

print(task_3(3, 2))

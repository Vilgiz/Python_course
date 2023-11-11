## Вычисление корня без "from math import sqrt" с использыванием функции

def sqrt(target):
    x = 1
    oldx = None
    while oldx != x:
        oldx = x
        x = (x + target / x) / 2
    return x

target = int(input(f'Введите число, из которого нужно высчислить корень: \n'))

result = sqrt(target)
print(round(result, 3))
print(round(result * result, 3))

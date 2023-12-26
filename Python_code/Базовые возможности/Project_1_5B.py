
# TODO: 1. Дан список температурных изменений в течение дня (целые числа). Известно,
# что измеряющее устройство иногда сбоит и записывает отсутствие
# температуры (значение None). Выведите среднюю температуру за
# наблюдаемый промежуток времени, предварительно очистив список от
# неопределенных значений. Гарантируется, что хотя бы одно определенное
# значение в списке есть.

def average_temp(temp_list):
    """
    Вычисляет среднюю температуру из списка, исключая значения None.

    Args:
        temp_list (list): Список температур.

    Returns:
        float: Средняя температура, округленная до двух знаков после запятой.
    """
    temp_list = [temp for temp in temp_list if temp is not None]
    average = sum(temp_list) / len(temp_list)
    return round(average, 2)

# TODO: 2. Напишите функцию, которая принимает неограниченное количество
# числовых аргументов и возвращает кортеж из двух списков: отрицательных
# значений (отсортирован по убыванию); неотрицательных значений
# (отсортирован по возрастанию).

def sort_from_zero(input_list):
    """
    Разделяет список на два списка: значения меньше нуля и значения больше или равные нулю.

    Args:
        input_list (list): Входной список чисел.

    Returns:
        list: Кортеж из двух списков: значения меньше нуля и значения больше или равные нулю.
    """
    less_zero = filter(lambda x: x < 0, input_list)
    more_zero = filter(lambda x: x >= 0, input_list)
    return list(less_zero), list(more_zero)


def my_sort(input_list):
    """
    Сортирует список, разделяя его на значения меньше нуля и значения больше или равные нулю.

    Args:
        input_list (list): Входной список чисел.

    Returns:
        tuple: Кортеж из двух списков: значения меньше нуля (в обратном порядке) и значения больше или равные нулю.
    """
    less_zero, more_zero = sort_from_zero(input_list)
    less_zero.sort(reverse=True)
    more_zero.sort()
    return less_zero, more_zero



# TODO: 3. Составьте две функции для возведения числа в степень: один из вариантов
# реализуйте в рекурсивном стиле.

def power_my(num, power):
    """
    Возведение числа в степень.

    Args:
        num (float): Число, которое нужно возвести в степень.
        power (int): Степень, в которую нужно возвести число.

    Returns:
        float: Результат возведения числа в степень, округленный до двух знаков после запятой.
    """
    res = num
    for _ in range(power-1):
        res = res * num
    return round(res, 2)

def power_recursive(num, power):
    """
    Возведение числа в степень с использованием рекурсии.

    Args:
        num (float): Число, которое нужно возвести в степень.
        power (int): Степень, в которую нужно возвести число.

    Returns:
        float: Результат возведения числа в степень, округленный до двух знаков после запятой.
    """
    if power == 0:
        return 1
    elif power < 0:
        return round(1 / power_recursive(num, -power), 2)
    else:
        return round(num * power_recursive(num, power - 1), 2)

def power(num, power):
    """
    Возведение числа в степень с использованием оператора **.

    Args:
        num (float): Число, которое нужно возвести в степень.
        power (int): Степень, в которую нужно возвести число.

    Returns:
        float: Результат возведения числа в степень, округленный до двух знаков после запятой.
    """
    return round(num ** power, 2)

if __name__ == "__main__":
    # task 1
    # print (average_temp([10, 8, 6, None, 5, 2, 0, -0, -1, -5, None, -5, -3, 0, 1, 4, 6]))
    
    # task 2:
    print(my_sort([1,3,2,6,4,5,7,9,8,-1,-3,-2,-6,-5,-4]))
    
    # task 3:
    # print(power_my(5,2))
    # print(power_recursive(5,2))
    # print(power(5,2))
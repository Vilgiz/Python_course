from random import randint
import numpy as np
import names

# TODO: Задание 1. Создайте список случайно сгенерированных чисел от 1 до 100. На
# основе этого списка создайте второй, который будет содержать слова “High”
# ("высокий”) или “Low” ("низкий") в зависимости от того, больше или меньше
# соответствующее число исходного списка некого порогового значения (само
# значение порога должно быть задано вами произвольно как значение переменной).

def task_1():
    
    random_list = [randint(1, 100) for _ in range(10)]
    threshold = 50
    result_list = ['High' if i > threshold else 'Low' for i in random_list]
    
    for i in range(len(random_list)):
        print(random_list[i], "-" ,result_list[i])

# TODO: Задание 2. Создайте список из 100 имен. Для генерации 100 имен можно
# воспользоваться примером из прошлого модуля Random_names.py в котором
# применялся модуль names (его потребуется инсталлировать с помощью pip). На
# основе этого списка имен создайте два новых списка. Один с именами, где первый
# символ начинается с буквы между “А” и “М”, а другой – содержит остальные имена.

def task_2():
    lastname = np.array([''.join(names.get_last_name()) for _ in range(100)])
    firstname = np.array([''.join(names.get_first_name()) for _ in range(100)])
    Names = list(zip(firstname, lastname))

    alphabet = [chr(i) for i in range(ord('A'), ord('N'))]

    AM_name = []
    else_name = []

    for name in Names:
        if name[0][0] in alphabet:
            AM_name.append(name)
        else:
            else_name.append(name)
    
    print(f"\n corted list:")
    for i in range(len(AM_name)):
        print(AM_name[i])
    
    print(f"\n remaining list:")
    for i in range(len(else_name)):
        print(else_name[i])
        
    print(len(else_name),len(AM_name))
    
# TODO: Задание 3. Акростих. Пользователь вводит в консоль слова по одному. Когда
# пользователь введет пустую строку (что означает окончание ввода), программа
# должна вывести слово, составленное из первых букв введенных пользователем слов

def task_3():
    words = []
    while (True):
        word = (input("Введите слово:\n").lower()).replace(" ","")
        if word == "":
            break
        words.append(word)
    result(words)
       
def result(words):
    acrostic = ''.join(word[0] for word in words)
    print(acrostic.replace(" ",""))


if __name__ == "__main__":
    # task_1()
    # task_2()
    task_3()
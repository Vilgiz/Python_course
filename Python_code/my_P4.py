from random import randint
import time

#Ввод имен играющих
gamer1 = input('Введите имя 1-го играющего ')
gamer2 = input('Введите имя 2-го играющего ')

resulting_points_gamer1 = 0
resulting_points_gamer2 = 0

number_of_throws = int(input('Введите количество бросков '))

for i in range(number_of_throws):
    #Моделирование бросания кубика первым играющим
    print('Кубик бросает', gamer1)
    time.sleep(1)
    n1 = randint(1, 6)
    print('Выпало:', n1)
    resulting_points_gamer1 += n1

    #Моделирование бросания кубика вторым играющим
    print('Кубик бросает', gamer2)
    time.sleep(1)
    n2 = randint(1, 6)
    print('Выпало:', n2)
    resulting_points_gamer2 += n2
    

if resulting_points_gamer1 > resulting_points_gamer2:
    print('Выиграл', gamer1)
elif resulting_points_gamer1 < resulting_points_gamer2:
    print('Выиграл', gamer2)
else:
    print('Ничья')
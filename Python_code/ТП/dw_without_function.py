## Вычисление корня без "from math import sqrt" без использывания функции

target = int(input('Введите число, из которого нужно вычислить корень: ')) 
x = 1 
oldx = None 
while oldx != x: 
    oldx = x 
    x = (x + target / x) / 2 
 
rounded_result = round(x, 3) 
rounded_square = round(x * x, 3) 
 
print(rounded_result) 
print(rounded_square) 
''' Задание 1 '''

param = int(input())
result = ((param > 5)  *  (param <= 30) * (param - 5) 
          * 1.2 + (param > 30) * (param - 30) * 1.5)

print(result)  



''' Задание 2 '''

n = int(input())
flag = False

flag = (n%2 == 0) or flag

print(flag)
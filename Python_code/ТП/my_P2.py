 ### TODO: Работа со строками

string1 = "This is a string. "
string2 = " This is another string."


print(string1 + string2)

print(len(string1)) # определяет длину строки;
print(string1.title()) # преобразует первый символ каждого слова в строке к верхнему регистру;
print(string1.lower()) # символы строки преобразуются к нижнему регистру;
print(string1.upper()) # символы строки преобразуются к верхнему регистру;
print(string1.rstrip()) # удаляются пробелы в конце строки;
print(string1.lstrip()) # удаляются пробелы в начале строки;
print(string1.strip()) # удаляются пробелы с обоих концов;
print(string1.strip('0')) # удаляются с обоих концов указанные символы в параметре функции.

d = "qwerty"
ch = d[2] # извлекается символ 'e'
print(f"ch\n")
chm = d[1:3]
print(f"{chm} срез c 1 по 3\n")
chm = d[1:]
print(f"{chm} срез c 1 последний\n")
chm = d[:3]
print(f"{chm} срез c 0 по 3\n")
chm = d[:]
print(f"{chm} c 0 по последний \n")
chm = d[1:5:2]
print(f"{chm} срез первых двух символов c 1 по 5\n")

 
try:
    d[2] = 'o' 
except:
    print("TypeError: 'str' object does not support item assignment")
    
 ### TODO: Работа с числами
 
a = 4
b = 3
 
print(f"{a/b} - целочисленное деление(\),\n")
print(f"{a%b} - взятие остатка \n")
print(f"{a**b} - возведение в степень \n")

param = "string"
 
try:
    param +=  a
except:
    print("TypeError: can only concatenate str (not int) to str")
    
# * Вариант решения:

param += str(a)
print(f"{param} - сделали явное предобразования типа данных \n")  



 ### TODO: Преобразование данных
 
""" n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3) """

 ### TODO: Форматирование строк
 
a = 1/3
print("{:7.3f}".format(a))

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))


 
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(str(float(n1)) + " plus " + str(float(n2)) + " = " + str(float(n3))) 

print("{:7.3f}".format(float(n1)) + " + " 
      + "{:7.3f}".format(float(n2)) + " = ", 
      "{:7.3f}".format(float(n3)))

print("{:10.3e}".format(float(n1)) + " + " 
      + "{:10.3e}".format(float(n2)) + " = ", 
      "{:10.3e}".format(float(n3)))

 ### TODO: Списки
 
list1 = [82,8,23,97,92,44,17,39,11,12]

#dir(list)

#help(list.insert)

list1[0] = 0



list1.append(1)

print(list1)

list1.insert(2, 100)

print(list1)

list1.remove(0)

print(list1)



list1.sort()

print(list1)

list2 = [3,5,6,2,33,6,11]
print(list2)
lis = sorted(list2)

print(list2)

 # TODO: Кортежи

dir(tuple)
help(tuple.index)
help(tuple.count)


seq = (2,8,23,97,92,44,17,39,11,12)
 
print(seq) 
print(seq.count(8))
print(seq.index(44))

print(seq) 
 
listseq = list(seq) 

print(listseq) 
type(listseq)
 
 
 # TODO: Словари
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}

print(D)

D['food'] = "Orange"
D['quantity'] += 10

print(D)

dp = {}

quantity = int(input())

for i in range(0, quantity):
    name = input()
    age = input()
    dp[name] = age

print(dp)
 
 # TODO: Вложенность хранения данных
 
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'}, 
       'job': ['dev', 'mgr'], 'age': 25}

print(f"Полное имя: {rec['name']['firstname']} {rec['name']['lastname']}") 
print(f"Имя: {rec['name']['firstname']}") 
print(f"Список должностей: {', '.join(rec['job'])}") 
 
rec['job'].append('janitor') 

print(f"Полное имя: {rec['name']['firstname']} {rec['name']['lastname']}") 
print(f"Возраст: {rec['age']}") 
print(f"Список должностей: {', '.join(rec['job'])}")
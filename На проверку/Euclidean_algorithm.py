

def euclidean_algorithm(a, b): 
    while a != b: 
        if a > b: 
            a = a - b 
        else: 
            b = b - a 
    return a 
 
a = int(input('Задайте первое число: ')) 
b = int(input('Задайте второе число: ')) 
 
nod = euclidean_algorithm(a, b) 
print('НОД равен', nod) 
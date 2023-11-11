

print("Введите год:")
year = int(input())
print("Введите номер программы:")
programm = int(input())


### * Через условные операторы  programm = 1 

if programm == 1:
    if year % 400 == 0:
        print(f"{year} - Это високосный год!")
    elif year % 100 == 0:
        print(f"{year} - Это не високосный год!")
    elif year % 4 == 0:
        print(f"{year} - Это високосный год!")
    else:
        print(f"{year} - Это не високосный год!")

### * Через тернарные операторы  programm = 2

if programm == 2:
    is_leap_year = "Это високосный год!" if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else "Это не високосный год!" 
    print(f"{year} - {is_leap_year}") 

### * Через операторы сравнения  programm = 3

if programm == 3: 
    is_leap_year = ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)) * "Это високосный год!" or "Это не високосный год!"
    print(is_leap_year)
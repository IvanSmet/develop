# name = input("Как вас зовут ? ")
# print("Привет,", name, '!')
# print('lol', 'ddd', 'kek', sep=('@@@@@'), end=('!!!'))
# print('qqq', 'www', 'eee', end=('!!!'))
# print ("Python", 'kek', 'hand', end='\n')
# print('po4emu')
# print('Mercury', 'Venus', sep='*', end='!')
# print('Mars', 'Jupiter', sep='**', end='?')
# print('sss', end='')
# print('dddddc')

# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')

# print('Раз', end='*')
# print('Два', end='*')
# print('Три', end='')

# print('Money often', end='##')
# print('costs', end='##')
# print('too much', end='')

# a = input()
# b = input()
# c = input()
# d = input()
# print(b, c, d, sep=a)

# a = input()
# print('Привет, ', a, end='!')

# name, surname = input(), input()
# print('Имя', name, 'Фамилия', surname)

# name1 = 'zalupa'
# name2 = 'polnaya'
# name1, name2 = name2, name1

# print('Python', end='=')
# print('C#', end='*')

# num1 = 7
# num2 = 10
# num3 = num1 + num2
# print(num3)

# a = 3
# b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# Функция int преобразует строковый тип данных в число
# s = '1992'  # Строковый тип данных
# year = int(s)  # Числовой тип данных
# print(year)

# Считывание целочисленных данных
# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)

# num = 17
# s = str(num)
# print(s)

# num1 = int(input())
# print(num1)
# print(num1 + 1)
# print(num1 + 2)

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# print(num1 + num2 + num3)

# num1 = int(input())
# print("Объем =", num1 * num1 * num1)
# print('Площадь полной поверхности =', 6 * (num1 * num1))

# a = int(input())
# b = int(input())
# f = 3 * ((a + b) * (a + b) * (a + b)) + (275 * (b * b)) - (127 * a) - 41
# print(f)

# num1 = int(input())
# print("Следующее за числом", num1, "число:", num1 + 1)
# print("Для числа", num1, "предыдущее число:", num1 - 1)

# monitor = int(input())
# sys_unit = int(input())
# keyboard = int(input())
# com_mouse = int(input())
# print((monitor + sys_unit + keyboard + com_mouse) * 3)

# num1 = int(input())
# num2 = int(input())
# lett1 = str(num1)
# lett2 = str(num2)

# print(lett1, "+", lett2, "=", num1 + num2)
# print(lett1, "-", lett2, "=", num1 - num2)
# print(lett1, "*", lett2, "=", num1 * num2)


# Этот кусок кода делает такуууую хуйнюююю
# num1 = int(input())
# num2 = int(input())
# print(num1, "+", num2, "=", num1 + num2)
# print(num1, "-", num2, "=", num1 - num2)
# print(num1, "*", num2, "=", num1 * num2)

# lol = int(input())
# d = int(input())
# n = int(input())
# print(lol + d * (n - 1))

# x = int(input())
# print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep="ХУЙ")

# b1 = int(input())
# q = int(input())
# n = int(input())
# print(b1 * q ** (n - 1))

# santimetrs = int(input())
# zalupa = santimetrs // 100
# print(zalupa)

# population = int(input())
# x = population % 2
# y = population // 2
# print(x + y)

# population = int(input()) + 1
# print(population // 2)

# population = int(input())
# x = population // 2
# print(population - x)

# Ёбаный поезд
# place = int(input())
# coupe = (place + 4 - 1) // 4
# print(coupe)

# place = -int(input())
# print(place // 4 * -1)

# minute = int(input())
# hour = minute // 60
# minutes = minute % 60
# print(minute, 'мин - это', hour, 'час', minutes, 'минут.')
"""
num = int(input())
# мы получаем число десятков
first_num = num // 10
# мы получаем число единиц
second_num = num % 10
print(first_num, second_num)
"""
# switch numbers
# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Искомое число =', last_digit * 10 + first_digit)

# num = int(input())
# first_n = num // 100
# middle_n = (num % 100) // 10
# last_n = num % 10

# summ = first_n + middle_n + last_n
# proizv = first_n * middle_n * last_n

# print("Сумма цифр =", summ)
# print("Произведение цифр =", proizv)

# num = int(input())
# one, two, three = (num // 10 ** 2) % 10, (num // 10 ** 1) % 10, (num // 10 ** 0) % 10
# print(one * 100 + two * 10 + three)
# print(one * 100 + three * 10 + two)
# print(two, one, three, sep="")
# print(two, three, one, sep="")
# print(three, one, two, sep="")
# print(three, two, one, sep="")

# num = int(input())
# one, two, three, four = (num // 10 ** 3) % 10, (num // 10 ** 2) % 10, (num // 10 ** 1) % 10, (num // 10 ** 0) % 10
# print("Цифра в позиции тысяч равна", one)
# print("Цифра в позиции сотен равна", two)
# print("Цифра в позиции десятков равна", three)
# print("Цифра в позиции единиц равна", four)

# n = int(input())
# print(n + n * 11 + n * 111)

answer = input("What is programming language we learning ?")
if answer == "Python":
    print("Python right !")
else:
    print("Wrong !")
    print("Zalupa")
    print("xaxaxaxaxa")
    print("lOk")

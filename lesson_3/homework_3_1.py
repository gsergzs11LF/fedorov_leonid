# задание 1
from Lesson_1.homework_1_1 import age

print('Привет, мир!')
print(5, 10, 15)
print(10 + 25)

# задание 2
print(1, 2, 3, sep=' & ')
print('Python', end=' ')
print('Лучший Язык')

# задание 3
x = 3.14
y = -8
print(f'Координаты точки: x = {x}, y = {y}')
name = str(input('Введи своё имя: '))
age = int(input('Введи свой возраст: '))
result = f'Тебя зовут {name} и тебе {age} лет'
print(result)

# задание 4
name1 = input('Введи свое имя!')
print(f'Привет, {name1}!')

# задание 5
a = float(input('Введи любое число:'))
b = float(input('Введи еще одно число:'))
result = a + b
print("Сумма чисел равна:", result)

a = int(input('Введи любое целое число: '))
result = a ** 2
print('Твое число в квадрате равно: ', result)

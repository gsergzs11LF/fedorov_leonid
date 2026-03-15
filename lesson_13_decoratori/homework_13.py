'''
++++++++++++++++++++++++++++++++++++++++++++++++
Декораторы в Python
++++++++++++++++++++++++++++++++++++++++++++++++
'''

'''
===============================================
1. Напишите декоратор uppercase_decorator, который делает результат выполнения функции прописными буквами.
Пример вызова:
@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())  # "HELLO, WORLD!"
===============================================
'''

# def uppercase_decorator(func):
#     def wrapper():
#         func()
#         res_1 = func().upper()
#         return res_1
#     return wrapper
#
# @uppercase_decorator
# def say_hello():
#     return 'hello, world!'
#
# print(say_hello())

'''
===============================================
2. Создайте декоратор repeat(n), который выполняет функцию n раз.
Пример вызова:
@repeat(3)
def hello():
    print("Hello!")
hello()
Вывод:
Hello!
Hello!
Hello!
===============================================
'''
# def deco_params(count):
#     def repeater(func):
#         def wrapper(*args, **kwargs):
#             i = count
#             while i != 0:
#                 func()
#                 i -= 1
#         return wrapper
#     return repeater
#
# @deco_params(10)
# def hello():
#     print('Hello!')
#
# hello()

'''
3. Создайте декоратор cache, который кэширует результаты выполнения функции.
Если функция вызывается с теми же аргументами – возвращать сохраненный результат вместо нового вычисления.
Пример вызова:
@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))  # 5 (результат взят из кэша)
'''

# def cashe(func):
#     cashe_1 = {}
#     def wrapper(*args, **kwargs):
#         key = args
#         if key in cashe_1:
#             print('Результат взят из кэша')
#             return cashe_1[key]
#         else:
#             res = func(*args,**kwargs)
#             cashe_1[key] = res
#             return cashe_1[key]
#
#     return wrapper
#
#
# @cashe
# def slow_add(a, b):
#     print(f"Вычисляю {a} + {b}...")
#     return a + b
#
# print(slow_add(2,3))
# print(slow_add(2,3))
# print(slow_add(5,7))

'''
===============================================
4. Создайте декоратор с таймером timer(repeat), который выполняет функцию repeat раз и выводит среднее время выполнения.
Пример вызова:
@timer(3)
def slow_function():
    time.sleep(1)
slow_function()  # Среднее время выполнения: 1.0002 сек
'''
import time

def timer(repeat):
    def deco(func):
        def wrapper(*args, **kwargs):
            i = repeat
            total_time = 0
            while i != 0:
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                i -= 1
                total_time += end - start
                print('Время выполнения:', end - start)
            avg = total_time / repeat
            return avg
        return wrapper
    return deco

@timer(5)
def slow_function():
    print('Вызов функции')
    time.sleep(2)
print("Среднее время выполнения:", slow_function())
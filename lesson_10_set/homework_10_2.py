'''
++++++++++++++++++++++++++++++++++++++++++++++++
Генераторы множеств и словарей
++++++++++++++++++++++++++++++++++++++++++++++++
'''

'''
1. Создайте множество из квадратов чисел от 1 до 10, но только для четных чисел.
'''
set_1 = {x ** 2 for x in range(1, 11) if x % 2 == 0}
print (set_1)

'''
2. Дан список:
words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
Создайте множество уникальных слов, преобразовав их в верхний регистр.
'''
words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
set_words = {w.upper() for w in words}
print(set_words)

'''
3. Дан словарь:
grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
Используя генератор, создайте новый словарь, где:
Если оценка больше или равна 80, записать "отлично".
Если меньше 80, записать "удовлетворительно".
решил чуть усложнить и дополнить задание
'''
grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
grades_dict = {
              name : f'Отлично, твоя оценка {x}' if x >= 80
              else f'Удовлетворительно, твоя оценка {x}'
              for name, x in grades.items()
}
print(grades_dict)

'''
4. Дано множество слов:
text = {"Python", "automation", "programming", "testing"}
Создайте новый словарь, где ключи – это слова из множества, а значения – длина каждого слова.
'''
text = {"Python", "automation", "programming", "testing"}
dict_1 = {key: len(key) for key in text}
print(dict_1)

'''
5. Создайте вложенный словарь, где ключи – числа от 1 до n (для примера пусть n = 10), 
а значения – множества квадратов чисел от 1 до ключа.
Пример для n = 3:
{
1: {1},
2: {1, 4},
3: {1, 4, 9}
}
'''

# n = 10
# result = {}
# for key in range(1, n + 1):
#     set_1 = {x ** 2 for x in range(1, key + 1)}
#     result[key] = set_1
# print(result)

n = 10
result = {
    key : {x ** 2 for x in range(1, key+1)}
    for key in range(1, n+1)
}
print(result)




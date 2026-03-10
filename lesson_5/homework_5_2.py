# задание 1
from idlelib.replace import replace

cities1 = ['Saratov', 'Samara', 'Stavropol', 'Moscow']
cities2 = cities1[:]
print(id(cities1), cities1)
print(id(cities2), cities2)

# задание 2
print(cities1[1:3])
print(cities1[2:])
print(cities1[:3])
print(cities1[:])
print(cities1[-2:])

# задание 3
print(cities1[1::2])
print(cities1[::-1])
print(cities1[-1::-2])

# задание 4
cities1[1:2] = ['Сочи', 'Нижний Новгород']
print(cities1)
cities1[1::2] = ['Город'] * len(cities1[1::2])
print(cities1)

cities2[1:3]
print(cities2[1:3])
cities2[1:3] = "Волгоград", "Омск"
print(cities2)

# задание 5
a = [1, 2, 3]
b = [4, 5, 6]
result = a + b
print(result)

c = ["Python", "rocks"]
result1 = c * 2
print(result1)

# задание 6
d = [1, 2, 3]
e = [1, 2, 3]
print(d == e)
print([10, 5, 3] > [5, 10, 3])
# print([1, 2, 3] > [1, 2, 'abc']) # ошибка будет '>' not supported between instances of 'int' and 'str'

# задание 7
chars = list("Python")
print('chars: ', chars)
print(max(chars))
# print(sum(chars))  будет ошибка, нельзя складывать






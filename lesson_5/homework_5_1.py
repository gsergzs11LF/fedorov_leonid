# задание 1
cities = ['Москва', 'Тверь', 'Вологда'] #список с строковыми элементами
numbers = [1, 2, 3, 4, 5] #список с целыми числами
mixed = [1, 2, 3, 'test', 1.23, True, [1, 2], False] #список с разными элементами

# задание 2
print(cities[0])
print(numbers[-1])
# print(cities[10]) тут будет ошибка list index out of range

# задание 3
numbers[1] = 10
print(numbers)
mixed[-1] = 'Python'
print(mixed)

# задание 4
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# задание 5
a = [1, 2, 3]
b = [4, 5]
c = a + b
print(c)

d = ['Python', 'is', 'awesome']
print(d * 3)

# задание 6
print(3 in numbers)
print('Москва' in cities)
print([1, 2] in mixed)

# задание 7
del numbers[2]
print(numbers)
del cities[-1]
print(cities)

# задание 8
p = 'Python'
p = list(p)
print(p)
print(max(p))
print(min(p))
# print(sum(p)) будет ошибка так как складывать нельзя




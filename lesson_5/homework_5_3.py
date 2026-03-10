# задание 1
numbers = [5, 10, 15]
numbers.append(20)
numbers.insert(2, 7)
numbers.append('Python')
print(numbers)

# задание 2
numbers.remove(10)
print(numbers)
a = numbers.pop()
print(numbers)
print(a)
a = numbers.pop(1)
print(a)
a = numbers.clear()
print(a)

# задание 3
letters = ["a", "b", "c"]
b = letters.copy()
print(letters, id(letters))
print(b, id(b))
c = list(letters)
print(c, id(c))

# задание 4
marks = [2, 3, 5, 3, 4, 5, 2, 3]
print(marks.count(3)) #
print(6 in marks, marks.index(5)) #Проверь, содержится ли число 6 в списке перед вызовом index().

# задание 5
nums = [8, 2, 5, 1, 7]
print('список nums: ', nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)

# задание 6
cities = ["Город 2", "Город 3", "Город 1"]
cities.sort()
print(cities, id(cities))
cities_2 = sorted(cities)
print(cities_2, id(cities_2))

# задание 7
chars = list("programming")
print(chars.count('g'))
chars.reverse()
print(chars)
chars.sort()
print(chars) #список станет в алфавитном порядке идти






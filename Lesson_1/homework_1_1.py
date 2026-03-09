# Задание 1
import keyword

name = "Леонид"
age = 23
height = 174.9
print("Имя:",name,"Возраст:",age,"Рост:",height)

# задание 2
x = 10
print(type(x))
x = 25.5
print(type(x))
x = 'Python'
print(type(x))

# задание 3
a = 7
b = a
print(a, b)
a = 10
print(b)
# все просто - когда мы создали объект 7 - 'a' ссылается на эту 7, потом мы сказали чтобы b тоже ссылался
# на объект 7. После чего мы создали новый объект "10", на который ссылается "a", а b все так же продолжает
# ссылаться на старую 7

# задание 4
x = y = z = 100
print(x,y,z)
print(id(x), id(y), id(z)) #одинаковые id
x, y, z = 100, 101, 102
print(x, y ,z)
print(id(x), id(y), id(z)) #тут будут разные id

# задание 5
a = 5
b = 10
a, b = b, a
print(a, b) # выведет что а = 10 а б = 5

# задание 6
# True = 10 нельзя
# print = 11 нельзя
# if = 12 нельзя
print(keyword.kwlist) # выведет список слов

# задание 7
var1 = 42
var2 = 3.14
var3 = 'Hello'
print(type(var1), type(var2), type(var3))
var1 = 'test string'
print(type(var1))

# задание 8
country = "Россия"
region = "Ставропольский край"
city = "Ставрополь"
population = 563103
year_of_foundation = 1777
print(type(country))
print(type(region))
print(type(city))
print(type(population))
print(type(year_of_foundation))
переменная = 10
print(переменная) #работает!



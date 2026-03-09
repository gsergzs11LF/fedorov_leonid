# задание 1
print(5 > 3)
print(10 < 2)
print(7 == 7)
print(6 != 8)
print(4 >= 4)
print(9 <= 3)
res = 8 > 12
print(type(res))

# задание 2
x = 15
print(f'Является ли число {x} четным:', x % 2 == 0)
print(f'Делится ли число {x} на 5 без остатка:', x % 5 == 0)
print(f'Делится ли число {x} на 5 и на 3 одновременно без остатка:', (x % 5 == 0) and (x % 3 ==0))

# задание 3
y = 4.5
print(y >= 1 and y <= 10)
print((0 <= y <= 5) or (10 <= y <= 15))
print(not (y < 5))

# задание 4
print(True or False and False) #сначала and потом or
print(not False and True) #сначала not False (true) потом and
print(False or not False and True) #сначала not False and True (true) потом False
print(10 > 5 or 3 < 1) # or в конце выполняется

# задание 5
print((bool(0))) #false потому что 0
print((bool(-5))) #true потому что число
print((bool(3.14))) #true потому что число
print((bool(""))) #false потому что пустая строка
print((bool("Python")))#true потому что есть инфа в строке
print((bool(" ")))#true потому что есть инфа в строке

# задание 6
n = 10
print(f'Является ли число {n} положительным, четным и делится ли на 3: ', (n > 0) and (n % 2 == 0) and (n % 3 == 0))


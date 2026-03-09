#задание 1
s1 = 'Python'
s2 = 'Программирование'
print(s1, s2)
s3 = '''
вот такая большая многострочная строка
можно на несколько строк выводить
и будет отлично вообще
'''
print(s3)
empty = ''
print("Длина пустой строки: ", len(empty))

#задание 2
first_name = "Иван"
last_name = "Петров"
full_name = first_name + ' ' + last_name
print('Полное имя с пробелом:', full_name)

#задание 3
s = 'Возраст: '
age = 25
print(s + str(age))

#задание 4
a = 'ха'
print('ха' * 4)
# print('ха' * 2.5) тут будет ошибка, так как только на целые числа можно умножать

#задание 5
text = 'Привет, мир!'
print("Длина строки: ", len(text))
text2 = ""
print("Длина строки2: ", len(text2))

#задание 6
sentence = "Я изучаю Python"
print('Python' in sentence)
print('Java' in sentence)

#задание 7
a1 = 'apple'
b1 = 'banana'
print('apple == banana: ', a1 == b1)
print('apple != banana: ', a1 != b1)
print('apple < banana: ', a1 < b1)
print('apple > banana: ', a1 > b1)
print('apple >= banana: ', a1 >= b1)
print('apple <= banana: ', a1 <= b1)

#задание 8!
print(ord("А"))
print(ord("а"))
print(ord("Я"))
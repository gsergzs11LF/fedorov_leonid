# задание 1
s = "Python для автоматизации"
print('Верхний регистр:', s.upper())
print('Нижний регистр:', s.lower())

# задание 2
msg = 'абракадабра'
print('Сколько ра в слове абракадабра: ', msg.count('ра'))
print('Сколько а начиная с 3его символа в слове абракадабра: ', msg.count('а', 2)) #считаем количество "а" начиная со второго индекса (или с 3ей буквы)

# задание 3
print('Первое вхождение буквы а: ', msg.find('ка')) #выведет 4
print('Последнее вхождение буквы а: ', msg.rfind('а')) #выведет 10 так как 10 это последняя буква
print('Поиск несуществующих символов: ', msg.find('xyz')) #выведет -1, так как это метод find, если бы был index была бы ошибка

# задание 4
text = 'Я изучаю Java'
new_text = text.replace('Java', 'Python') #меняем джава на питон
print(new_text)
new_text2 = new_text.replace(' ', '') #удаляем все пробелы
print(new_text2)

# задание 5
print('Состоит ли Питон только из букв: ', 'Python'.isalpha())
print('Состоит ли 12345 только из цифр: ', '12345'.isdigit())
print('Строка 12345abc состоит не только из цифр: ', not '12345abc'.isdigit()) #добавил здесь not так как вопрос звучит - Строка 12345abc не только из цифр (ответ true так как она действительно состоит не только из цифр)

# задание 6
code = '42'
print(code.rjust(5, '0'))
print('text'.ljust(10, '*'))

# задание 7
fruit = 'яблоко, груша, банан'
fruit_1, fruit_2, fruit_3 = fruit.split()
print(fruit_1, fruit_2, fruit_3)

a = 'Python;Java;C++'
a_1, a_2, a_3 = a.split(';')
print(a_1, a_2, a_3)

# задание 8
b = ["Привет", "мир", "!"]
print(' '.join(b))

fruit2 = ["apple", "banana", "cherry"]
print(', '.join(fruit2))

# задание 9
print(" Python".lstrip())
print("Python ".rstrip())
print(" Python ".strip())

# задание 10
text3 = "программирование"
text3_new = 'П' + text3[1:]
text3_new2 = text3.capitalize() #сделает начала строки с большой буквы (как вариант такой использовать)
text3_count = text3.count('р')
text3_find = text3.find('и')
text3_reverse = text3[::-1]
print(text3_new)
print(text3_count)
print(text3_find)
print(text3_reverse)


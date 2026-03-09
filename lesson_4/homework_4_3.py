# задание 1
name = 'Leonid'
age = "23"
age2 = 23
print('Меня зовут ' + name + ' мне ' + age + ' лет') #работает потому что age строка
# print('Меня зовут: ' + name + ' мне ' + age2 + ' лет') #не работает потому что age int
#надо вот так
print('Меня зовут ' + name + ' мне ' + str(age2) + ' лет')

# задание 2
print('Меня зовут {0} и мне {1} лет'.format(name, age))
print('Меня зовут {imya} и мне {vozrast} лет'.format(imya = name, vozrast = age))
print('Меня зовут {imya} и мне {vozrast} лет'.format(vozrast = age, imya = name)) #с измененным порядком тоже работает

# задание 3
city = 'Stavropol'
year = '2026'
print(f'Сегодня {year} год и я живу в городе {city}')
print(f'Через 5 лет будет {int(year) + 5} год') #тут перевел в int чтобы выполнить сложение

# задание 4
print(f'Дважды мой возраст: {int(age) * 2}')
print(f'Дважды мой возраст: {int(age) * 2}'.upper())

# задание 5
dollar = 3
exchange_rate = 92.5 * dollar
result = 'Курс валют: {0} доллар = {1} рубля.'.format(dollar, exchange_rate) #можем менять количество долларов и будет считаться сколько это в рублях
print(result)

x = 9
x_v_kvadrate = x ** 2
print(f'Квадрат числа {x} равен {x_v_kvadrate}')




a = 2
b = 0.5

print(a + b)

name = 'Анастасия'

print(f'Привет, {name}!')

v = int(input('Введите число от 1 до 10: '))

print(v + 10)

name = input('Введите ваше имя: ')

print(f'Привет {name}! Как дела?')

a = float('1')  # 1.0
print(a)

b = int('2.5')  # ValueError: invalid literal for int() with base 10: '2.5'
print(b)

c = bool(1)  # True
print(c)

d = bool('')  # False
print(d)

i = bool(0)  # False
print(i)

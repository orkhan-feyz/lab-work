import math
print('-------Задание 1.1--------')
x   =  4.5

for y in range(20,31,2):
    y = y/10

    an_rad = math.acos(y/x)
    an = math.degrees(an_rad)
    print('Задача 1 Способ 1',an)


print('-------Задание 1.2--------')
x   =  4.5
y = 1.8
while y < 3:
    y+=0.2

    an_rad = math.acos(y/x)
    an = math.degrees(an_rad)

    print(' Задача 1 Способ 2 ',an)



print('-------Задание 2--------')

def valid_dx():
    while True:
        try:
            dx = float(input("Введите целое число dx > 0: "))
            if dx > 0:
                return dx
            else:
                print("Число должно быть больше 0")
        except ValueError:
            print("Нужно ыелое число")

x0 = float(input('X0: '))
x1 = float(input('x1: '))
dx = valid_dx()


while x<= x1 + dx /2:
    if x < 0:
        z = x ** 2
    elif 0 < x <= 1:
        z = math.sin(x)
    else:
        z = math.cos(x)
    print(z)
    x+=dx



print('-------Задание 3--------')


def valid_n():
    while True:
        try:
            n = int(input("Введите целое число n (n > 0): "))
            if n > 0:
                return n
            else:
                print("Число должно быть больше 0")
        except ValueError:
            print("Нужно ыелое число")

x = float(input("Введите вещественное число x: "))
n = valid_n()


summ = 1.0
term = 1.0

for i in range(1, n + 1):
    term *= x / i
    summ += term

print(f"Приближенное значение:" , summ)

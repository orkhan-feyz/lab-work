import random

def get_m():
    while True:
        try:
            m = int(input("Введите размер матрицы M: "))
            if m <= 0:
                print("Размер должен быть больше 0!")
                continue
            return m
        except ValueError:
            print("Ошибка! Введите целое число.")

m = get_m()
    
matrix = [[random.randint(-10, 10) for j in range(m)] for i in range(m)]

for row in matrix:
    s = 0
    for x in row:
        if x > 0 and x % 2 == 0:
            s += x
    row.append(s)


print("Исходная матрица")
for row in matrix:
    print(row)

for i in range(m - 1):
    for j in range(m - 1 - i):
        if matrix[j][-1] < matrix[j+1][-1]:
            matrix[j],matrix[j+1] = matrix[j+1],matrix[j]
                
print("\nИзмененная матрица после сортировки:")
for row in matrix:
    print(row)
        
print("Характеристики после сортировки:", [row[-1] for row in matrix])




import random

while True:
    try:
        n = int(input("Введите размер словаря: "))
        if n > 0:
            break
        print("Ошибка! Размер должен быть > 0")
    except ValueError:
        print("Ошибка! Введите целое число")

d = {}
for i in range(n):
    d["кл" + str(i + 1)] = random.randint(1, 100)

print("Исходный словарь:", d)

print("\nДобавление")
new_k = input("Введите ключ (строка): ")
while True:
    try:
        new_v = int(input("Введите значение (целое число): "))
        break
    except ValueError:
        print("Ошибка! Введите целое число")

print("Словарь ДО:", d)
d[new_k] = new_v
print("Словарь ПОСЛЕ:", d)

print("\n--- Поиск ---")
find_k = input("Введите ключ для поиска: ")
if find_k in d:
    print("Значение:", d[find_k])
else:
    print("Не найдено!")

print("\nУдаление")
del_k = input("Введите ключ для удаления: ")
print("Словарь ДО:", d)
if del_k in d:
    del d[del_k]
    print("Словарь ПОСЛЕ:", d)
else:
    print("Такого ключа нет\nСловарь не изменился:", d)

print("Ключи словаря:", list(d.keys()))


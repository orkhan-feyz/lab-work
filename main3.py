# Лаба 5
def func_isalpha(s):
    bad_s = '0123456789 ,.!?-()[]{}<>_@#№$%^&*+=|\\/:"`~;'
    if not s or s == " " * len(s):
        return False

    for char in s:
        if char in bad_s:
            return False
    return True


def val_word():
    while True:
        try:
            word = input('Введите слово для поиска:  ')
            if len(word) != 0 and func_isalpha(word):
                return word
            else:
                print('Проверьте написание слова')
        except:
            print('Ошибка')


def val_text():
    while True:
        try:
            text = input('Введите текст')
            if len(text) == 0:
                print('Текст не может быть пустым')
            else:
                return text
        except:
            print('Ошибка')


text = val_text()
word = val_word()

words_list = []
last_index = 0
for i in range(len(text)):
    if len(words_list) >= 1 and text[i] == ' ':
        words_list.append(text[last_index:i])
        last_index = i + 1

    if len(words_list) == 0 and text[i] == ' ':
        words_list.append(text[0:i])
        last_index = i + 1
        
if last_index < len(text):
    words_list.append(text[last_index:])

c = 0 
for i in range(len(words_list)):

    if word == words_list[i]:
        c+=1

print(f'{word} встречается в тексте: {c}')


def val_stroka():
    while True:
        try:
            stroka = input('Введите строку: ')
            if len(stroka) == 0:
                print('Проверьте написание строки')
            return stroka
        except:
            print('Ошибка')
stroka = val_stroka()

sym = 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмё'

c = 0 
for i in range(len(stroka)):
    for a in range(len(sym)):
        if stroka[i] == sym[a]:
            c+=1
print(f'Общее кол-во строчных лат и рус букв в строке: {c}')



from random import randint
def val_size():
    while True:
        try:
            n = int(input('Введите размер списка N:'))
            if n <= 0:
                print('введите положительное число')
            else:
                return n
        except ValueError:
            print('Ошибка')
def val_c():
    while True:
        try:
            c = float(input('Число C: '))
            return c
        except ValueError:
            print('Ошибка')
            
size = val_size()
n = [randint(-1000,1000) for _ in range(size)]
c = val_c()

summ = 0 
for i in range(len(n)):
    if c>n[i]:
        summ += n[i]

print(f'Сумма эл меньше {c}: {summ}')

elements = []
for i in range(len(n) - 1, -1, -1):
    if float(n[i]) >= 0:
        elements.append(int(n[i]))
    else:
        break

summ = 0 
for i in range(len(elements)):
    summ += elements[i]
print(f'Сумма целых чисел от последнего отрицат: {summ}')



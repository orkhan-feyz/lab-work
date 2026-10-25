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
        last_index += i
        print(text[last_index], text[i], words_list, last_index)

    if len(words_list) == 0 and text[i] == ' ':
        words_list.append(text[0:i])
        last_index += 1

print(words_list)
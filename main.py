

#пример 

d = {
    'Россия':['РНД','МСК'],
    'Китай':['Пекин'],
}

cou = input('Введите страну ').strip()
city = input('Введите город ').strip()

if cou in d:
    if city in d[cou]:
        print('страна и город уже добавлены')

    else:
        d[cou].append(city)
        print(f'Город {city} добавлен')
else:
    d[cou] = [city]
    print('Страна добавлена и город в ней ')

for i,c in d.items():
    print(f'Страна {i}')
    print(f'Города: {','.join(c)}')


mx_city = -1
mx_cou = None
for i,c in d.items():
    if len(c) > mx_city:
        mx_city = len(c)
        mx_cou = i
print(f'Страна с наибольшим кол городов - {mx_cou} - городов {mx_city}')
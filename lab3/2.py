a = input('Введите текст:')
with open('proba2.txt', 'w', encoding='utf-8') as file:
    file.write(a)

a = input('Введите текст:')
with open('proba2.txt', 'a', encoding='utf-8') as file:
    file.write(a)



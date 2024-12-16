filename = input("Введите имя файла: ")
try:
    with open(filename, 'r') as f:
        print("Содержимое файла:", f.read())
except FileNotFoundError:
    print("Файл не найден")

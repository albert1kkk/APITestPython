import requests
import os
import fnmatch

def func():
    print(
        "1. Создать товар \n2. Редактировать товар \n3. Получить информацию о товаре \n4. Найти товар через Поиск \n5. Добавить картнику к товару \n6. Удалить товар \n7. Провести все этапы \n0. Завершить проверку")
    command = input("Введите номер нужного пункта: ")
    if command == "1":
        create()
    elif command == "2":
        update()
    elif command == "3":
        getinfo()
    elif command == "4":
        searchitem()
    elif command == "5":
        uploadimg()
    elif command == "6":
        deleteitem()
    elif command == "7":
        print("Создание товара")
        create()
        print("Изменение товара")
        update()
        print("Получение информации о товаре")
        getinfo()
        print("Поиск товара по параметрам")
        searchitem()
        print("Добавление картинки к товару")
        uploadimg()
        print("Удаление товара")
        deleteitem()
    elif command == "0":
        print("Завершение...")
        quit()
    else:
        print("Вы ввели неправильное значение")


def create():
    name = input("Введите название товара: ")
    section = input("Введите раздел товара: ")
    description = input("Введите описание: ")
    price = input("Введите цену товара: ")
    body = {"name": name, "section": section, "description": description, "price": price}
    response = requests.post("http://shop.bugred.ru/api/items/create/", json=body)
    print(response.text)
    print(response)
    data = response.json()
    if data["status"] == "error":
        print("Проверка не пройдена \n")
    elif data["status"] == "ok":
        print("Проверка пройдена успешно \n")


def update():
    id = input("Введите ID товара: ")
    name = input("Введите название товара: ")
    section = input("Введите раздел товара: ")
    description = input("Введите описание: ")
    price = input("Введите цену товара: ")
    body = {"id": id, "name": name, "section": section, "description": description, "price": price}
    response = requests.post("http://shop.bugred.ru/api/items/update/", json=body)
    print(response.text)
    print(response)
    data = response.json()
    if data["status"] == "error":
        print("Проверка не пройдена \n")
    elif data["status"] == "ok":
        print("Проверка пройдена успешно \n")


def getinfo():
    id = input("Введите ID товара: ")
    payload = {"id": id}
    response = requests.get("http://shop.bugred.ru/api/items/get/", data=payload)
    print(response.text)
    print(response)
    data = response.json()
    if data["status"] == "error":
        print("Проверка не пройдена \n")
    elif data["status"] == "ok":
        print("Проверка пройдена успешно \n")


def deleteitem():
    id = input("Введите ID товара: ")
    payload = {"id": id}
    response = requests.get("http://shop.bugred.ru/api/items/delete/", data=payload)
    print(response.text)
    print(response)
    data = response.json()
    if data["status"] == "error":
        print("Проверка не пройдена \n")
    elif data["status"] == "ok":
        print("Проверка пройдена успешно \n")


def searchitem():
    query = input("Введите название товара: ")
    color = input("Введите цвет товара: ")
    price_from = input("Введите цену от: ")
    body = {"query": query, "color": color, "price_from": price_from}
    response = requests.get("http://shop.bugred.ru/api/items/search/", json=body)
    print(response.text)
    print(response)
    data = response.json()
    if data["status"] == "error":
        print("Проверка не пройдена \n")
    elif data["status"] == "ok":
        print("Проверка пройдена успешно \n")


def uploadimg():
    id = input("Введите ID товара: ")
    payload = {"id": id}
    print("Список картинок: ")
    fileslist = os.listdir('.')
    pattern = "*.jpg"
    for entry in fileslist:
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
    img = input("Введите название картинки (только .png): ")
    files = [('photo', ('file', open(img, 'rb')))]
    response = requests.post("http://shop.bugred.ru/api/items/upload_photo/", data=payload, files=files)
    print(response.text)
    print(response)
    data = response.json()
    if data["status"] == "error":
        print("Проверка не пройдена \n")
    elif data["status"] == "ok":
        print("Проверка пройдена успешно \n")



func()
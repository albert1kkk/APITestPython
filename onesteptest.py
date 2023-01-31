import requests
import os
import fnmatch
import random
from string import ascii_lowercase
from random import sample


def func():
    print("1. Создать товар \n2. Редактировать товар \n3. Получить информацию о товаре \n4. Найти товар через Поиск \n5. Добавить картнику к товару \n6. Удалить товар \n7. Провести все этапы \n0. Завершить проверку")
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
    name = "".join(sample(ascii_lowercase, 5)).capitalize()
    section = ["test", "Платья", "Брюки"]
    description = ["Красивый", "Элегантный", "Женственный", "Подчеркивающий"]
    price = random.randint(0, 5000)
    color = ["Красный", "Синий", "Синий"]
    body = {"name": name, "section": random.choice(section), "description": random.choice(description), "price": price, "color": random.choice(color)}
    response = requests.post("http://shop.bugred.ru/api/items/create/", json=body)
    print(response.text)
    print(response)
    data = response.json()
    if data["status"] == "error":
        print("Проверка не пройдена \n")
    elif data["status"] == "ok":
        print("Проверка пройдена успешно \n")
    itemid = open("itemid.txt", "w")
    itemid.write(data["result"]["id"])
    itemid.close()


def update():
    id = open("itemid.txt", "r")
    name = "".join(sample(ascii_lowercase, 5)).capitalize()
    section = ["test", "Платья", "Брюки"]
    description = ["Красивый", "Элегантный", "Женственный", "Подчеркивающий"]
    price = random.randint(0, 5000)
    body = {"id": id.read(), "name": name, "section": random.choice(section), "description": random.choice(description), "price": price}
    response = requests.post("http://shop.bugred.ru/api/items/update/", json=body)
    print(response.text)
    print(response)
    data = response.json()
    if data["status"] == "error":
        print("Проверка не пройдена \n")
    elif data["status"] == "ok":
        print("Проверка пройдена успешно \n")


def getinfo():
    id = open("itemid.txt", "r")
    payload = {"id": id.read()}
    response = requests.get("http://shop.bugred.ru/api/items/get/", data=payload)
    print(response.text)
    print(response)
    data = response.json()
    if data["status"] == "error":
        print("Проверка не пройдена \n")
    elif data["status"] == "ok":
        print("Проверка пройдена успешно \n")
    itemid = open("itemid.txt", "w")
    itemid.write(data["result"]["id"])
    itemid.close()
    itemcolor = open("color.txt", "w")
    itemcolor.write(data["result"]["color"])
    itemcolor.close()
    itemname = open("name.txt", "w")
    itemname.write(data["result"]["name"])
    itemname.close()
    itemprice = open("price.txt", "w")
    itemprice.write(str(data["result"]["price"]))
    itemprice.close()

def deleteitem():
    id = open("itemid.txt", "r")
    payload = {"id": id.read()}
    response = requests.get("http://shop.bugred.ru/api/items/delete/", data=payload)
    print(response.text)
    print(response)
    data = response.json()
    if data["status"] == "error":
        print("Проверка не пройдена \n")
    elif data["status"] == "ok":
        print("Проверка пройдена успешно \n")
    id.close()
    path = "itemid.txt"
    os.remove(path)
    path = "color.txt"
    os.remove(path)
    path = "price.txt"
    os.remove(path)
    path = "name.txt"
    os.remove(path)

def searchitem():
    query = open("name.txt", "r")
    color = open("color.txt", "r")
    price_from = open("price.txt", "r")
    body = {"query": query.read(), "color": color.read(), "price_from": price_from.read()}
    response = requests.get("http://shop.bugred.ru/api/items/search/", json=body)
    print(response.text)
    print(response)
    data = response.json()
    if data["status"] == "error":
        print("Проверка не пройдена \n")
    elif data["status"] == "ok":
        print("Проверка пройдена успешно \n")


def uploadimg():
    id = open("itemid.txt", "r")
    payload = {"id": id.read()}
    print("Список картинок: ")
    fileslist = os.listdir('.')
    pattern = "*.jpg"
    for entry in fileslist:
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
    img = input("Введите название картинки (только .jpg): ")
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
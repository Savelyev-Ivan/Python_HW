#Создать список и заполнить его элементами различных типов данных.
#Реализовать скрипт проверки типа данных каждого элемента.
#Использовать функцию type() для проверки типа.
#Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

ivan_list = [[5, 6], (0j + 1), 4, 8.8,
             True, 'str', TypeError, bytearray(b'sixteen'),
             range(22), {1: 'one', 2: 'two'}, {5, 6},
             (7, 8, 8.5), None, frozenset(), b'thirteen',
             zip(*[(9, 10), (11, 12), ('b','c')])]
for i, item in enumerate(ivan_list, 1):
    print(f"{i}) {item} - {type(item)}")
    
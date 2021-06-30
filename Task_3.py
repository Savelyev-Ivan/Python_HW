#Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
a = input("Введите аргумент 1: ")
b = input("Введите аргумент 2: ")
c = input("Введите аргумент 3: ")


def my_func(a, b, c):

    try:
        a, b, c = int(a), int(b), int(c)
        z = [a, b, c]
        z.remove(min(a, b, c))
        return sum(z)
    except ValueError:
        return "Аргумент - это число и сумму вы не получите"

print("Сумма двух наибольших аргументов: ")
print(my_func(a, b, c))
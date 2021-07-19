#Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#В рамках класса реализовать два метода.
#Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#Проверить работу полученной структуры на реальных данных.

import time


class Date:
    li_date = []

    def __init__(self, string_date: str):
        Date.li_date = string_date.split('-')

    @classmethod
    def convert(cls):
        for i, el in enumerate(cls.li_date):
            cls.li_date[i] = int(el)

    @staticmethod
    def validate(string_date: str):
        try:
            _ = time.strptime(string_date, '%d-%m-%Y')
        except ValueError:
            return "Error date"
        return "OK"


d = Date('19-07-2021')
print(d.li_date)
d.convert()
print(d.li_date)
print(Date.validate('19-06-2021'))
print(Date.validate('19-06-2022'))
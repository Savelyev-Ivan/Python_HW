#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
#Проверьте его работу на данных, вводимых пользователем.
#При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyZeroDivisionError(Exception):
    def __init__(self, msg):
        self.msg = msg


i_num = int(input("Давайте поделим число 50? Введите делитель:   "))
try:
    if i_num == 0:
        raise MyZeroDivisionError('Но на ноль делить нельзя(((')
    else:
        print(f"50 / {i_num} = {50 / i_num}")
except MyZeroDivisionError as err:
    print(err)
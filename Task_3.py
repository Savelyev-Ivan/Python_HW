#Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
#Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
#Пример файла:
#Иванов 23543.12
#Петров 13749.32


with open('text_3.txt', 'r+', encoding="utf-8") as file:
    lst = list()
    for line in file.readlines():
        lst.extend(line.rstrip().split(' '))
print(lst)

print("\nОклад меньше 20000 у сотрудников: ")
summ = 0
for i in range(1, len(lst), 2):
    a = float(lst[i])
    summ += a
    count = len(lst) / 2
    if a <= 20000:
        print(lst[i-1])
middle_profit = summ / count
print("\nСредняя зарплата сотрудников: ", "%.1f" % middle_profit)
#Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


f = open('text_05.txt', 'w', encoding="utf-8")
print("Введите набор чисел, разделенных пробелами, для завершения программы нажмите Enter: ")

while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break

f = open('text_05.txt', 'r', encoding="utf-8")
list = f.read().split()
total = 0
for elem in list:
    total += float(elem)
print("Сумма чисел в файле: ", total)
f.close()
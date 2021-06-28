#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.

month = int(input("Enter month number from 1 till 12: "))
my_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
           10: "October", 11: "November", 12: "December"}
my_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
           "October", "November", "December"]
i = None
if 0 < month < 3:
    i = "Winter"
if 2 < month < 6:
    i = "Spring"
if 5 < month < 9:
    i = "Summer"
if 8 < month < 12:
    i = "Autumn"
if month == 12:
    i = "Winter"
if month in my_dict:
    print(f"{month}th month of year - this {my_dict[month]}")
    print(f"{month}th month of year - this {my_list[month - 1]}")
    print(f"{month}th month of year - this {i}")

else:
    print("Wrong number")
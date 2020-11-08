# Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_month = int(input("Введите месяц целым числом: "))

# Решение через list
month = ""
month_list = [["Зима", 12, 1, 2], ["Весна", 3, 4, 5], ["Лето", 6, 7, 8], ["Осень", 9, 10, 11]]
for i in range(len(month_list)):
    if month_list[i].count(user_month):
        month = month_list[i][0]
print(month)

# Решение через dict
month_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна',
              4: 'Весна', 5: 'Весна', 6: 'Лето',
              7: 'Лето', 8: 'Лето', 9: 'Осень',
              10: 'Осень', 11: 'Осень', 12: 'Зима'}

print(month_dict.get(user_month))

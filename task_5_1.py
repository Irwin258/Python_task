# Задача 1.
# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
user_str = str
f_obj = open("task_5_1.txt", "w", encoding='utf-8')
while user_str != "":
    user_str = input("Введите данные:")
    f_obj.writelines(user_str + '\n')
f_obj.close()


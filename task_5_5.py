# Задача 5
# Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open("task_5_5.txt", 'w+', encoding='utf-8') as f_obj:
    f_obj.writelines(input("Введите числа через пробел: "))
    f_obj.seek(0)
    my_str = f_obj.readlines()
    my_str = (" ".join(my_str)).split()
    my_str = sum(list(map(int, my_str)))
    print(my_str)





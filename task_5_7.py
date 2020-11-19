# Задание 7
# Создать (не программно) текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью. Если фирма получила убытки, т
# акже добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

average_profit = 0
firm_list = []
profit_list = []
with open("task_5_7.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        my_list = line.split()
        if int(my_list[2]) > int(my_list[3]):
            firm_list.append(my_list[0])
            profit_list.append(int(my_list[2]) - int(my_list[3]))
            average_profit += int(my_list[2]) - int(my_list[3])
        else:
            firm_list.append(my_list[0])
            profit_list.append(int(my_list[2]) - int(my_list[3]))

average_profit = {"average_profit": average_profit}
my_list = dict(zip(firm_list, profit_list)), average_profit
with open("my_file.json", "w") as write_f:
    json.dump(my_list,write_f)
print(my_list)



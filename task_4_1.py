# Задача 1
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать
# формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import sys


def payment():
    output_hours = int(sys.argv[1])
    hours = int(sys.argv[2])
    prize = int(sys.argv[3])
    print(output_hours * hours + prize)


payment()

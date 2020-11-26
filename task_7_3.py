# Задача 3
# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# целочисленное (с округлением до целого) деление клеток, соответственно.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n**.


class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        print(f'Новыя клетка с количеством ячеек =  {self.num + other.num}')
        self.num = self.num + other.num
        return self

    def __sub__(self, other):
        if self.num - other.num <= 0:
            print("Вычитание клеток невозможно")
        else:
            print(f'Новыя клетка с количеством ячеек =  {self.num - other.num}')
            self.num = self.num - other.num
            return self

    def __mul__(self, other):
        print(f'Новыя клетка с количеством ячеек =  {self.num * other.num}')
        self.num = self.num * other.num
        return self

    def __floordiv__(self, other):
        print(f'Новыя клетка с количеством ячеек =  {self.num // other.num}')
        self.num = self.num // other.num
        return self

    def make_order(self, num_row):
        my_str = ''
        for i in range(self.num // num_row):
            my_str += '*' * num_row + '\n'
        my_str += '*' * int(self.num % num_row)
        return my_str


cell_1 = Cell(17)
cell_2 = Cell(15)
new_cell = cell_1 + cell_2

print(new_cell.num)

print(new_cell.make_order(7))

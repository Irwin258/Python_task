# Задача 1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования
# матрицы.Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы. Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for i in self.matrix:
            for el in i:
                res += f'{el} '' '
            res += f'\n'
        return f'{res}'

    def __add__(self, other):
        new_matrix = []
        if len(self.matrix) != len(other.matrix):
            return "Размеры матриц не совпадают"
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                return "Размеры матриц не совпадают"
            a = [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            new_matrix.append(a)
        new_matrix = Matrix(new_matrix)
        return new_matrix


mat_1 = Matrix([[45, 45], [54, 54], [666, 45]])
mat_2 = Matrix([[46, 46], [54, 54], [666, 45]])
mat_3 = Matrix([[45, 46], [54, 54], [666, 45], [666, 45]])
print(f'Матрица  1:\n{mat_1}')
print(f'Матрица  2:\n{mat_2}')
print(f'Матрица  2:\n{mat_3}')
res = mat_1 + mat_2
print(f'Сумма матриц 1 и 2:\n{res}')
res = mat_1 + mat_3
print(f'Сумма матриц 1 и 3:\n{res}')
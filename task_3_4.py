# Задача 4
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла

def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1/result


print(my_func_1(2, -6))
print(my_func_2(2, -6))

# Задача 3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, agr_2, agr_3):
    x = [arg_1, agr_2, agr_3]
    x.remove(min(x))
    y = sum(x)
    return y


print(my_func(56, 6, 70))

# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.


# a, b = [int(x) for x in input(f'Введите через пробел два неотрицательных числа,чтобы узнать сумму: ', ).split()]
# a = int(input("Введите число: "))
# b = int(input("Введите его степень: "))

# def exp(a, b):
#     if (b == 1):
#         return a
#     if (b != 1):
#         return (a * exp(a, b - 1))

# print("Результат возведения в степень =", exp(a, b))


# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


# a, b = [int(x) for x in input(f'Введите через пробел два неотрицательных числа,чтобы узнать сумму: ', ).split()]

# def summa(a, b):
#     a += 1
#     b -= 1
#     if b > 0:
#         return summa(a, b)
#     else:
#         return a
 
 
# print (summa(a, b))
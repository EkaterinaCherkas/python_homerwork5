# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))

def sum_numbers(a, b):
    if b == 0:
        return a
    return (sum_numbers(a , b - 1) + 1)

print(f'Sum of numbers {a} and {b} = {sum_numbers(a, b)}')
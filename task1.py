# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))

def power_number(a, b):
    if b == 1:
        return a
    return a * power_number(a, b - 1)

print(f'{a} to the power of {b} = {power_number(a, b)}')
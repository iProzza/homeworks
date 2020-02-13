# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def s_div():
    try:
        first_n = float(input('Введите первое число: '))
        sec_n = float(input('Введите второе число: '))
        gen_n = first_n / sec_n
    except ZeroDivisionError:
        print('Деление на ноль')
        return
    return gen_n
print(s_div())
#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    num = [a, b, c]
    num.remove(min(a, b, c, key=int))
    return sum(num)
print(my_func(90, 8, 4))
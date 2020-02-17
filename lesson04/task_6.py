# 6. Реализовать два небольших скрипта:начиная с указанного,
# а) бесконечный итератор, генерирующий целые числа,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.


from itertools import count, cycle

for z in count(-100):   # 1
    print(z)
    if z > 99:
        break


phone = ['xiaomi', 'iphone', 'samsumg', 'Huawei', 'Sony']   # 2
iter = cycle(phone)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))








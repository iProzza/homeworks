# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('5.txt', 'w') as f:
    nums = input('Введите целые числа через пробел: ')
    f.write('Введите числа: ' + nums + '\n')
    nums = map(int, nums.split())  # without list
    sum_nums = sum(nums)
    f.write('Сумма чисел: ' + str(sum_nums))
    print('Сумма введуных чисел:', sum_nums)
print('Все записано в файл')

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def g_unit(name, surname, birth, city, email, phone):
    print(name, surname, birth, city, email, phone)
g_unit(name='', surname='', birth='', city='', email='', phone='')
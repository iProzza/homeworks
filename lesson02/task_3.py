# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

mon = int(input('Введите номер месяца: '))
year = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
for key in year.keys():
    if mon in year[key]:
        print(key)
        break

# со словарем легко

month = int(input('Введите номер месяца: '))
#winter = [1, 2, 12]
#spring = [3, 4, 5]
#summer = [6, 7, 8]
#autumm = [9, 10, 11]
#year = ['winter', 'spring', 'summer', 'autumm']
#year = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#print(year[0])
for season in year:
    if month == 1 or 2 or 12:
        season = 'winter'
        print(season)
        break
    elif month == 3 or 4 or 5:
        season = 'spring'
        print(season)
        #break
    #elif month == 6 or 7 or 8:
        #break
    #elif month == 9 or 10 or 11:
        #season = 'осень'
        #print(season)
        #break


# со списком, не понял как input прикрепить к списку и через цикл вывести
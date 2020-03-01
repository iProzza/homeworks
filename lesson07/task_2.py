# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Garment:
    def __init__(self, size, high):
        self.size = size
        self.high = high

    def get_area_с(self):
        return self.size / 6.5 + 0.5

    def get_area_b(self):
        return self.high * 2 + 0.3

    @property
    def get_area_f(self):
        return str(f'общая площадь ткани {(self.size / 6.5 + 0.5) + (self.high * 2 + 0.3)}')


class Cloak(Garment):
    def __init__(self, size, high):
        super().__init__(size, high)
        self.area_с = self.size / 6.5 + 0.5

    def __str__(self):
        return f'площадь на плащ {self.area_с}'


class Blouse(Garment):
    def __init__(self, size, high):
        super().__init__(size, high)
        self.area_b = self.high * 2 + 0.3

    def __str__(self):
        return f'площадь на кофту {self.area_b}'


cloak = Cloak(10, 2)
blouse = Blouse(8, 4)
print(cloak)
print(blouse)
print(cloak.get_area_f)
print(blouse.get_area_f)
print(cloak.area_с)
print(blouse.area_b)



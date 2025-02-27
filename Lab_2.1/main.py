# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Table:
    def __init__(self,
                 count_of_legs: int,
                 material: str):
        """
        Создание и подготовка к работе объекта "Стол"
        :param count_of_legs - Число ножек стола
        :param material - Материал
        Пример:
        >>> table_1 = Table(5,"steel")
        """
        self.count_of_legs = count_of_legs
        if not isinstance(count_of_legs, int):
            raise TypeError("Количество ножек стола должно быть типа int")
        if not count_of_legs > 0:
            raise ValueError("Количество ножек стола должно быть положительным числом")

        self.material = material
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")

    def is_table_of_glass(self,) -> None: #Проверяет стеклянный ли стол?
        """
        Проверяет стеклянный ли стол

         Примеры:
        >>> table_2 = Table(5,"steel")
        >>> table_2.is_table_of_glass()
        """

    def is_table_of_steel(self, material: str):  # Проверяет стальной ли стол?
        """Проверяет стальной ли стол

         Примеры:
        >>> table_2 = Table(5,"steel")
        >>> table_2.is_table_of_steel()
        """

    def add_leg(self, legs_to_add: int): #Добавляет legs_to_add ножек стола
        """
        Добавляет количество ножек

        :param legs_to_add количество ножек, которые необходимо добавить
        :return: конечное число ножек

        Пример:
        >>> table_3 = Table(3, "steel")
        >>> table_3.add_leg()
        """
        if not isinstance(legs_to_add, int):
            raise TypeError("Количество ножек стола должно быть типа int")
        if not isinstance(legs_to_add, int):
            raise TypeError("Количество ножек стола должно быть типа int")


    def remove_leg(self): #Спиливает 1 ножку стола
        """
        Спиливает 1 ножку стола

        Пример:
        >>> table_4 = Table(4,"wood")
        >>> table_4.remove_leg()
        """
        if not count_of_legs > 1:
            raise ValueError("Количество ножек стола должно быть числом большим, чем единица")


class House:
    def __init__(self,
                 count_of_floors: int,
                 height_of_floor: [int, float]):
        """
        Создание и подготовка к работе объекта "Здание"

        :param count_of_floors - Число этажей
        :param height_of_floor - Высота этажа

        :raise TypeError Если типы аргументов не соответствуют ожидаемым
        :raise ValueError: Если значения аргументов не допустимы (например, отрицательные значения)

        Примеры:
               >>> house = House(5,4.4)
        """

        if not isinstance(count_of_floors, int):
            raise TypeError("Количество этажей должно быть типа int")
        if count_of_floors < 0:
            raise ValueError("Количество этажей должно быть положительным числом")
        if not isinstance(height_of_floor, (int, float)):
            raise TypeError("Количество этажей должно быть типа int или float")
        if height_of_floor < 0:
            raise ValueError("Высота этажа должна быть положительным числом")

        self.count_of_floors = count_of_floors
        self.height_of_floor = height_of_floor

    def add_floor(self):
        """
        Добавляет 1 этаж к существующему зданию

        :return: Выводит конечное количество этажей
        Примеры:
        >>> house_1 = House(3,3.0)
        >>> house_1.add_floor()
        """
        ...
    def change_floor(self, change_height_of_floor: [int, float]) -> int:
        """
        Изменяет высоту этажа на change_height_of_floor
        :param change_height_of_floor: Изменение высоты этажа
        :return: Результирующая высота этажа
        Примеры:
        >>> house_2 = House(3,2.8)
        >>> house_2.change_floor(2.4)
        """

        if not isinstance(change_height_of_floor, (int, float)):
            raise TypeError("Количество этажей должно быть типа int или float")

class CupOfTea:
    def __init__(self,
                 volume: int,
                 volume_of_tea: int):
        """
        Создание и подготовка к работе объекта "Стол"
        :param volume - Объем
        :param volume_of_tea - Объем чая в кружке
        Пример:
        >>> сupOfTea_1 = CupOfTea(500,300)
        """

        if not isinstance(volume, int):
            raise TypeError("Объем кружки должен быть типа int")
        if volume < 0:
            raise ValueError("Объем кружки должен быть положительным числом")
        if not isinstance(volume_of_tea, (int, float)):
            raise TypeError("Объем чая должену быть типа int или float")
        if volume_of_tea < 0:
            raise ValueError("Объем чая не может быть отрицательным")
        if volume_of_tea > volume:
            raise ValueError("Объем чая не может быть больше объема кружки")

        self.volume = volume
        self.volume_of_tea = volume_of_tea

    def is_cup_empty(self):
        """
        Проверяет пустая ли кружка?


        :return: Определяет пустая ли кружка?
        >>> сupOfTea_2 = CupOfTea(330,0)
        """
        ...

    def how_to_full_cup(self):
        """
        Определяет сколько еще налить чая в кружку, чтобы он был полон

        :return: Возвращает объем чая, который необходимо долить в кружку
        >>> сupOfTea_3 = CupOfTea(330,4)
        """
        ...


if __name__ == "__main__":

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()


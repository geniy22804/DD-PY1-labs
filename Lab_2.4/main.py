if __name__ == "__main__":
    from typing import Any


    class Animal:
        """
        Базовый класс, представляющий животное.
        """

        def __init__(self, name: str, age: int) -> None:
            """
            Конструктор базового класса.
            :param name: Имя животного.
            :param age: Возраст животного.
            """
            self._name = name  # Инкапсулируемое поле, так как имя не должно изменяться напрямую
            self._age = age  # Инкапсулируемое поле, так как возраст не должен изменяться напрямую

        def __str__(self) -> str:
            """
            Возвращает строковое представление животного.
            """
            return f"Животное: {self._name}, возраст: {self._age} лет"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта для отладки.
            """
            return f"Animal(name={self._name!r}, age={self._age!r})"

        def make_sound(self) -> str:
            """
            Возвращает звук, который издаёт животное.
            Должен быть переопределён в дочерних классах.
            """
            return "Неизвестный звук"


    class Dog(Animal):
        """
        Класс, представляющий собаку.
        """

        def __init__(self, name: str, age: int, breed: str) -> None:
            """
            Конструктор класса Dog.
            :param name: Имя собаки.
            :param age: Возраст собаки.
            :param breed: Порода собаки.
            """
            super().__init__(name, age)
            self._breed = breed  # Инкапсулируем, так как порода не изменяется после создания объекта

        def __str__(self) -> str:
            """
            Перегружаем метод для более информативного описания собаки.
            """
            return f"Собака породы {self._breed}: {self._name}, возраст: {self._age} лет"

        def make_sound(self) -> str:
            """
            Переопределяем метод make_sound, так как собака лает.
            """
            return "Гав-гав"


    class Cat(Animal):
        """
        Класс, представляющий кошку.
        """

        def __init__(self, name: str, age: int, color: str) -> None:
            """
            Конструктор класса Cat.
            :param name: Имя кошки.
            :param age: Возраст кошки.
            :param color: Окрас кошки.
            """
            super().__init__(name, age)
            self._color = color  # Инкапсулируем, так как цвет не должен изменяться после создания

        def make_sound(self) -> str:
            """
            Переопределяем метод make_sound, так как кошка мяукает.
            """
            return "Мяу-мяу"


    pass

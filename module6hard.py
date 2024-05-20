import colorsys, math


class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def __str__(self):
        pass

    def get_color(self):  # возвращает список RGB цветов
        return colorsys.rgb_to_hls(0, 0, 0)

    def __is_valid_color(self, r, g, b):  # служебный, принимает параметры r, g, b
        self.r = r
        self.g = g
        self.b = b
        if r or g or b < 0:
            if r or g or b > 255:
                print('Некорректный цвет, введите еще раз')

    def set_color(self, r, g, b):  # принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения
        self.r = r
        self.g = g
        self.b = b
        self.__color = self.set_color
        return self.__color

    def set_sides(self, *args):  # принимает неограниченное кол-во сторон
        self.args = args
        if self.set_sides == self.sides_count:
            self.__sides = self.set_sides
        else:
            self.__sides = self.args


    def __is_valid_sides(self, set_sides):  # принимает неограниченное кол-во сторон, возвращает True если все стороны целые числа
        self.set_sides = set_sides
        if set_sides == int:
            return True
        else:
            return False

    def __len__(self):   #  возвращаeт периметр фигуры

        return len(self.__sides)


class Circle(Figure):
    sides_count = 1
    __radius = 2


    def __init__(self, color, filled):
        self.color = color
        self.filled = filled


    def get_square(self, radius):
        self.__radius = set_sides * 2 * math.pi

        self.square = math.pi * self.__radius ** 2
        return self.square




class Triangle(Figure):
    sides_count = [1, 1, 1]
    sideA = 4
    sideB = 4
    sideC = 4

    def __init__(self, __height, __sides, __color, filled):
        super().__init__(__sides, __color, filled)
        self.__height = __height
        self.__sides = [1, 1, 1]
        self.__color = __color
        self.filled = filled

    def get_square(self, sideA, sideB, sideC):
        self.triangle_square = sideA + sideB + sideC // 2
        return self.triangle_square


class Cube(Figure):
    sides_count = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def __init__(self, color, filled):
        self.__height = 6

    def get_sides(self, __height):
        self.__height = 6

    def get_volume(self, __height):
        self.volume = __height**3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
#cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
#cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
#print(cube1.get_color())

# Проверка на изменение сторон:
#cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
#print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
#print(cube1.get_volume())

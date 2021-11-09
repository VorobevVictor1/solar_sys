# coding: utf-8
# license: GPLv3

"""class Space_object:
    """Тип данных, общий для всех космических объектов.
        Содержит массу, координаты, скорость объекта по осям х и у,
        силу, действующую на объект по осям х и у,
        а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, parameters):
        self.type = parameters[0]
        self.drawing_radius = int(parameters[1])
        self.drawing_color = parameters[2]
        self.mass = float(parameters[3])
        self.x = float(parameters[4])
        self.y = float(parameters[5])
        self.v_x = float(parameters[6])
        self.v_y = float(parameters[7])
        self.f_x = 0
        self.f_y = 0"""

class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    def __init__(self, parse_star_parameters(line, stars[line])):
        self.drawing_radius = int(stars[line][1])
        self.drawing_color = stars[line][2]
        self.mass = float(stars[line][3])
        self.x = float(stars[line][4])
        self.y = float(stars[line][5])
        self.v_x = float(stars[line][6])
        self.v_y = float(stars[line][7])
        self.f_x = 0
        self.f_y = 0


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self, parse_planet_parameters(line, stars[line])):
        self.drawing_radius = int(planets[line][1])
        self.drawing_color = planets[line][2]
        self.mass = float(planets[line][3])
        self.x = float(planets[line][4])
        self.y = float(planets[line][5])
        self.v_x = float(planets[line][6])
        self.v_y = float(planets[line][7])
        self.f_x = 0
        self.f_y = 0
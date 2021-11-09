# coding: utf-8
# license: GPLv3

class Space_object:
    """Тип данных, общий для всех космических объектов.
        Содержит массу, координаты, скорость объекта по осям х и у,
        силу, действующую на объект по осям х и у,
        а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, parameters):
        self.type = parameters[0]
        self.drawing_radius = parameters[1]
        self.drawing_color = parameters[2]
        self.mass = parameters[3]
        self.x = parameters[4]
        self.y = parameters[5]
        self.v_x = parameters[6]
        self.v_y = parameters[7]
        self.f_x = 0
        self.f_y = 0

class Star(Space_object):
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, parameters):
        super().__init__(parameters)



class Planet(Space_object):
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self, parameters):
        super().__init__(parameters)

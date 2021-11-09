# coding: utf-8
# license: GPLv3

from solar_objects import *
from solar_vis import DrawableObject


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """
    inp_space_object = open(input_filename)
    sol_obj = inp_space_object.read()
    inp_space_object.close()
    objects = sol_obj.split("#")
    print(objects)

    planets = []
    stars = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            object_string = line
            if object_type == "star":
                star = Star()
                stars_parameters = line.split()
                parse_star_parameters(line, star)
                stars.append(stars_parameters)
            elif object_type == "planet":
                planet = Planet()
                planets_parameters = line.split()
                parse_planet_parameters(line, planet)
                planets.append(planets_parameters)
            else:
                print("Unknown space object")
    print(stars, planets)

    return [DrawableObject(obj) for obj in objects]


def parse_star_parameters(line, stars[line]):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    return stars[line]
    pass  # FIXME: допишите парсер


def parse_planet_parameters(line, planets[line]):
    """Считывает данные о планете из строки.
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet.r = int(stars[line][1])
    planet.color = stars[line][2]
    planet.mass = int(stars[line][3])
    planet.x = int(stars[line][4])
    planet.y = int(stars[line][5])
    planet.Vx = int(stars[line][6])
    planet.Vy = int(stars[line][7])
    return planets[line]
    pass  # FIXME: допишите парсер


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME!


if __name__ == "__main__":
    print("This module is not for direct call!")
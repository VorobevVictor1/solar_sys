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

    space_objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star" or object_type == "planet":
                space_objects.append(parse_space_object_parameters(line))

            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in space_objects]

def parse_space_object_parameters(line):
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
    parameters = line.split()
    if line[0] == 'star':
        return Star(parameters)
    else:
        return Planet(parameters)



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

            object_line = ' '.join([str(obj.obj.type), str(obj.obj.drawing_radius), str(obj.obj.drawing_color),
                                    str(obj.obj.mass), str(obj.obj.x), str(obj.obj.y),
                                    str(obj.obj.v_x), str(obj.obj.v_y), '\n'])
            out_file.write(object_line)

if __name__ == "__main__":
    print("This module is not for direct call!")
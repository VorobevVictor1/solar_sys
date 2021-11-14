# coding: utf-8
# license: GPLv3
import math
gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.f_x, body.f_y = 0, 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        corner = math.atan2((obj.y - body.y), (obj.x - body.x))
        F = gravitational_constant * body.mass * obj.mass / (r)**2
        body.f_x += F * math.cos(corner)
        body.f_y += F * math.sin(corner)
        # FIXME: обработка аномалий при прохождении одного тела сквозь другое



def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    ax = body.f_x / body.mass
    body.v_x += ax * dt
    body.x += body.v_x * dt
    ay = body.f_y / body.mass
    body.v_y += ay * dt
    body.y += body.v_y * dt




def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")

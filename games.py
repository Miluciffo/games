import pyglet
import random

from pyglet import shapes
from pyglet.window import mouse

window = pyglet.window.Window(800, 800)
batch = pyglet.graphics.Batch()


def show_hero():
    hero_shape.x = hero_x
    hero_shape.y = hero_y


def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return (dx ** 2 + dy ** 2) ** .5


def show_enemy():
    for i in range(len(cord_list)):
        if distance(hero_x, hero_y, cord_list[i][0], cord_list[i][1]) < view_radius:
            enemy_shape_list[i].opacity = 255
            print(enemy_shape_list[i].opacity,'view')
        else:
            enemy_shape_list.opacity = 0
            # pass

view_radius = 100

hero_x = 400
hero_y = 400
hero_shape = shapes.Circle(hero_x, hero_y, radius=10, color=(0, 255, 0), batch=batch)

enemy_shape_list = []
cord_list = []
for i in range(10):
    cord_list.append([random.randint(5, 795), random.randint(5, 795)])  # [x,y]
    enemy_shape_list.append(
        shapes.Rectangle(x=cord_list[i][0], y=cord_list[i][1], width=10, height=10, color=(255, 0, 0), batch=batch))


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    global set_temp, temp_numb, time_flag


@window.event
def on_key_release(symbol, modifiers):
    global hero_x, hero_y
    # 0 - W 1-A 2-S 3-D
    if symbol == 119:
        # snake_cfg.dir_s = 0
        hero_y += 5
    if symbol == 97:
        # snake_cfg.dir_s = 1
        hero_x -= 5
    if symbol == 115:
        # snake_cfg.dir_s = 2
        hero_y -= 5
    if symbol == 100:
        hero_x += 5
        # snake_cfg.dir_s = 3
    show_hero()
    show_enemy()


pyglet.app.run()

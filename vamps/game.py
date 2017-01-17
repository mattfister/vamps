import pyglet
from pyglet.gl import *

from freezegame.image_loader import *

import freezegame.resources
from freezegame.image_loader import ImageLoader
from freezegame.abstract_state import AbstractState
from freezegame.sprite import Sprite
from freezegame.tile_map import TileMap
from freezegame.broad_phase_collision import RDC
from vamps.jumper import Jumper
import itertools
import math
from vamps.room import Room
from vamps.state_controller import StateController

pyglet.resource.path = ["./graphics"]
pyglet.resource.reindex()

freezegame.resources.images = ImageLoader('graphics')

platform = pyglet.window.get_platform()

debug_log = open('debug.txt', 'w')
print(platform)

debug_log.write(str(platform))

display = platform.get_default_display()

print(display)
debug_log.write(str(display))


screen = display.get_default_screen()
debug_log.write(str(screen))
print(str(screen))

debug_log.close()

template = pyglet.gl.Config(double_buffer=True)
config = screen.get_best_config(template=template)

window = pyglet.window.Window(1920, 1080, fullscreen=True, resizable=False, config=config, vsync=False)

icon16 = pyglet.image.load('graphics/pybaconIcon16.png')
icon32 = pyglet.image.load('graphics/pybaconIcon32.png')
window.set_icon(icon16, icon32)

window.set_caption("Freezegame Sample")

keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glShadeModel(GL_SMOOTH)

fps = pyglet.clock.ClockDisplay()


level = StateController()


@window.event
def on_resize(width, height):
    print(width)
    print(height)

    if height==0:
        height=1


def update(dt):
    level.update(dt, keys);

@window.event
def on_draw():
    window.clear()
    level.draw()
    fps.draw()
    #pyglet.gl.glFlush()
    #pyglet.gl.glFinish()


@window.event
def on_mouse_press(x, y, button, modifiers):
    level.handle_mouse_press(x, y, button, modifiers)


@window.event
def on_mouse_release(x, y, button, modifiers):
    level.handle_mouse_release(x, y, button, modifiers)


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    level.handle_mouse_drag(x, y, dx, dy, buttons, modifiers)


@window.event()
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    level.handle_mouse_scroll(x, y, scroll_x, scroll_y)


@window.event()
def on_mouse_motion(x, y, dx, dy):
    level.handle_mouse_motion(x, y, dx, dy)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)#systemSettings.desiredFps)#)
    pyglet.app.run()




import pyglet
from pyglet.gl import *

from freezegame.image_loader import *

import freezegame.resources
from freezegame.image_loader import ImageLoader
from freezegame.abstract_state import AbstractState
from freezegame.sprite import Sprite
from freezegame.tile_map import TileMap
from vamps.player import Player

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

window = pyglet.window.Window(1024, 768, fullscreen=False, resizable=False, config=config, vsync=False)

icon16 = pyglet.image.load('sample_graphics/pybaconIcon16.png')
icon32 = pyglet.image.load('sample_graphics/pybaconIcon32.png')
window.set_icon(icon16, icon32)

window.set_caption("Freezegame Sample")

keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glShadeModel(GL_SMOOTH)

fps = pyglet.clock.ClockDisplay()

level = AbstractState()

class SampleScene(AbstractState):
    def __init__(self):
        AbstractState.__init__(self)
        self.batch = pyglet.graphics.Batch()
        self.player_group = pyglet.graphics.OrderedGroup(3)
        self.sprite_group = pyglet.graphics.OrderedGroup(2)
        self.map_group = pyglet.graphics.OrderedGroup(1)
        self.background_group = pyglet.graphics.OrderedGroup(0)

        self.sprites = []

        self.player = None

        self.width = 10
        self.height = 10

        self.map = TileMap(32, 32,  self.width, self.height, self, 'tileSet', [0, 192, 32, 32], self.map_group)
        self.map.build_surrounding_walls()
        self.map.auto_tile()

        self.camera = [0, 0]

        self.player = Player(5*32, 5*32, self)
        self.sprites.append(self.player)

    def draw(self):
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT);

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        self.batch.draw()
        glPopMatrix()

    def update(self, dt, keys):
        if dt > 0.05:
            return

        for sprite in self.sprites:
            if sprite.updatable:
                sprite.update(dt, keys, self)

        # Now we turn off all the sprites
        for sprite in self.sprites:
            sprite.on = False
        for sprite in self.sprites:
            if sprite.updatable:
                sprite.resolve_tile_map_collisions(self.map)

        # TODO figure out broad phase collision again

        # Now do narrow phase collision
        for sprite in self.sprites:
            for other_sprite in self.sprites:
                if sprite is not other_sprite:
                    sprite.resolve_sprite_collision(other_sprite, 'y')

        for sprite in self.sprites:
            for other_sprite in self.sprites:
                if sprite is not other_sprite:
                    sprite.resolve_sprite_collision(other_sprite, 'y')

        # Double check that no one resolved into a wall
        for sprite in self.sprites:
            sprite.resolve_tile_map_collisions(self.map)
            sprite.finish_resolution()
            sprite.update_sprite_pos()



level = SampleScene()


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



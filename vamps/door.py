from freezegame.sprite import Sprite
import pyglet


class Door(Sprite):
    def __init__(self, x, y, state):
        Sprite.__init__(self, x, y, [0, 0, 32, 32], state, 'sprites', [3*32, 3*32, 32, 32], state.batch, state.wall_map_group)
        self.is_door = True
        self.physical_to_sprites = False
        self.gravitic = False
        self.physical_to_walls = False
        self.sensor_for_sprites = True
        self.is_open = False
        self.create_animations()
        self.play_animation('closed')

    def open(self):
        self.is_open = True
        self.play_animation('open')

    def create_animations(self):
        self.add_animation('closed', [[3*32, 3*32, 32, 32]], fps=0.1)
        self.add_animation('open', [[4*32, 3*32, 32, 32]], fps=0.1)

    def update(self, dt, keys, state):
        pass

    def update_animations(self, dt, keys, state):
        pass
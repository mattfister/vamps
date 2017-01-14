from freezegame.sprite import Sprite
import pyglet
from vamps.enemy import Enemy


class Roamer(Enemy):
    def __init__(self, x, y, facing, state):
        Enemy.__init__(self, x, y, facing, 3, [0, 0, 32, 32], state, 'sprites', [0, 3*32, 32, 32], state.batch, state.player_group)
        self.double_jump_power = True
        self.double_jump_space_up = False
        self.double_jump_available = False
        self.create_animations()
        self.facing = facing
        self.damage = 1

    def create_animations(self):
        self.add_animation('walkRight', [[0, 3*32, 32, 32], [1*32, 3*32, 32, 32]], fps=10.0)
        self.add_animation('walkLeft', [[0, 4*32, 32, 32], [1*32, 4*32, 32, 32]], fps=10.0)

    def update(self, dt, keys, state):
        acc = 1000.0
        jump = 300.0

        if self.facing == "left":
            self.vx += -acc * dt
            if self.collide_left:
                self.facing = "right"
        else:
            self.vx += acc * dt
            if self.collide_right:
                self.facing = "left"

        Enemy.update(self, dt, keys, state)

    def update_animations(self, dt, keys, state):
        if self.facing == 'right':
            self.play_animation('walkRight')
        elif self.facing == 'left':
            self.play_animation('walkLeft')

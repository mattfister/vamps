import random
from vamps.enemies.enemy import Enemy


class SeekingEagle(Enemy):
    def __init__(self, x, y, facing, state):
        Enemy.__init__(self, x, y, facing, 3, [0, 0, 32, 32], state, 'sprites', [1*32, 11*32, 32, 32], state.batch, state.enemy_group)
        self.create_animations()
        self.facing = facing
        self.gravitic = False
        self.damage = 1
        self.shoot_timeout = 2.0
        self.shoot_timer = random.uniform(0.1, self.shoot_timeout)
        self.dead_zone = 32


    def create_animations(self):
        self.add_animation('flyRight', [[1*32, 11*32, 32, 32], [2*32, 11*32, 32, 32]], fps=10.0)
        self.add_animation('flyLeft', [[1*32, 12*32, 32, 32], [2*32, 12*32, 32, 32]], fps=10.0)

    def update(self, dt, keys, state):
        vector_to_player = self.vector_to_player()
        if vector_to_player[0] > self.dead_zone:
            self.facing = 'right'
        elif vector_to_player[0] < -self.dead_zone:
            self.facing = 'left'

        if self.facing == "left":
            self.vx = -200
        else:
            self.vx = 200


        self.shoot_timer -= dt

        if self.shoot_timer <= 0.0:
            self.shoot_timer = self.shoot_timeout
            self.shoot('down')

        Enemy.update(self, dt, keys, state)

    def update_animations(self, dt, keys, state):
        if self.facing == 'right':
            self.play_animation('flyRight')
        elif self.facing == 'left':
            self.play_animation('flyLeft')

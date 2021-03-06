from vamps.enemies.enemy import Enemy


class Roamer(Enemy):
    def __init__(self, x, y, facing, state):
        Enemy.__init__(self, x, y, facing, 3, [0, 0, 32, 32], state, 'sprites', [1*32, 3*32, 32, 32], state.batch, state.enemy_group)
        self.create_animations()
        self.facing = facing
        self.damage = 1

    def create_animations(self):
        self.add_animation('walkRight', [[1*32, 3*32, 32, 32], [2*32, 3*32, 32, 32]], fps=10.0)
        self.add_animation('walkLeft', [[1*32, 4*32, 32, 32], [2*32, 4*32, 32, 32]], fps=10.0)

    def update(self, dt, keys, state):
        acc = 1000.0
        jump = 300.0

        if self.facing == "left":
            self.vx = -200
            if self.collide_left and self.on_ground:
                self.facing = "right"
        else:
            self.vx = 200
            if self.collide_right and self.on_ground:
                self.facing = "left"

        Enemy.update(self, dt, keys, state)

    def update_animations(self, dt, keys, state):
        if self.facing == 'right':
            self.play_animation('walkRight')
        elif self.facing == 'left':
            self.play_animation('walkLeft')

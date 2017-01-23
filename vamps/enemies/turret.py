from vamps.enemies.enemy import Enemy


class Turret(Enemy):
    def __init__(self, x, y, facing, state):
        Enemy.__init__(self, x, y, facing, 3, [0, 0, 32, 32], state, 'sprites', [1*32, 3*32, 32, 32], state.batch, state.enemy_group)
        self.create_animations()
        self.facing = facing
        self.shoot_timeout = 2.0
        self.shoot_timer = self.shoot_timeout
        self.gravitic = False
        self.damage = 1

    def create_animations(self):
        self.add_animation('walkRight', [[1*32, 3*32, 32, 32], [2*32, 3*32, 32, 32]], fps=10.0)
        self.add_animation('walkLeft', [[1*32, 4*32, 32, 32], [2*32, 4*32, 32, 32]], fps=10.0)

    def update(self, dt, keys, state):
        acc = 1000.0
        jump = 300.0

        self.shoot_timer -= dt

        if self.shoot_timer <= 0.0:
            self.shoot_timer = self.shoot_timeout
            self.shoot('player')

        Enemy.update(self, dt, keys, state)

    def update_animations(self, dt, keys, state):
        if self.facing == 'right':
            self.play_animation('walkRight')
        elif self.facing == 'left':
            self.play_animation('walkLeft')

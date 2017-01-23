from vamps.enemies.enemy import Enemy


class Eagle(Enemy):
    def __init__(self, x, y, facing, state):
        Enemy.__init__(self, x, y, facing, 3, [0, 0, 32, 32], state, 'sprites', [1*32, 3*32, 32, 32], state.batch, state.enemy_group)
        self.create_animations()
        self.facing = facing
        self.gravitic = False
        self.damage = 1
        self.shoot_timeout = 2.0
        self.shoot_timer = self.shoot_timeout

    def create_animations(self):
        self.add_animation('flyRight', [[1*32, 3*32, 32, 32], [2*32, 3*32, 32, 32]], fps=10.0)
        self.add_animation('flyLeft', [[1*32, 4*32, 32, 32], [2*32, 4*32, 32, 32]], fps=10.0)

    def update(self, dt, keys, state):
        acc = 1000.0
        jump = 300.0

        if self.facing == "left":
            self.vx = -200
            if self.collide_left:
                self.facing = "right"
        else:
            self.vx = 200
            if self.collide_right:
                self.facing = "left"

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

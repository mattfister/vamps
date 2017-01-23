from freezegame.sprite import Sprite
import pyglet
from freezegame.tile import Tile
from freezegame.vector_math import norm, vector_object_object


class EnemyMissile(Sprite):
    def __init__(self, x, y, direction, state):
        Sprite.__init__(self, x, y, [8, 8, 16, 16], state, 'sprites', [5*32, 2*32, 32, 32], state.batch, state.enemy_missile_group)
        self.create_animations()
        self.direction = direction
        self.play_animation('idle')
        self.speed = 500
        self.physical_to_sprites = False
        self.physical_to_walls = False
        self.sensor_for_sprites = True
        self.sensor_for_walls = True
        self.gravitic = False
        self.frictional = False
        self.is_missile = True
        self.life_timer = 1.5
        self.damages_player = True
        self.damage = 1
        if self.direction == 'right':
            self.vx = self.speed
        elif self.direction == 'left':
            self.vx = -self.speed
        elif self.direction == 'up':
            self.vy = self.speed
        elif self.direction == 'down':
            self.vy = -self.speed
        elif self.direction == 'player':
            if self.state.player is None:
                self.vx = 1
                self.vy = 0
            else:
                unit_vector_to_player = norm(vector_object_object(self, self.state.player))
                self.vx = unit_vector_to_player[0] * self.speed
                self.vy = unit_vector_to_player[1] * self.speed

    def create_animations(self):
        self.add_animation('idle', [[5*32, 3*32, 32, 32], [6*32, 3*32, 32, 32]], fps=10.0)

    def update(self, dt, keys, state):
        Sprite.update(self, dt, keys, state)
        self.life_timer -= dt
        if self.life_timer <= 0.0:
            self.dead = True

    def collision_callback(self, other_sprite):
        if other_sprite.is_player:
            other_sprite.take_damage(self.damage)
        if other_sprite.physical_to_sprites and not other_sprite.is_enemy and not other_sprite.is_missile:
            self.dead = True

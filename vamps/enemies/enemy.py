from freezegame.sprite import Sprite
import pyglet
from vamps.enemy_missile import EnemyMissile


class Enemy(Sprite):
    def __init__(self, x, y, facing, hp, box, state, image_name, image_region, batch, group):
        Sprite.__init__(self, x, y, box, state, image_name, image_region, batch, group)
        self.facing = facing
        self.hp = hp
        self.is_enemy = True
        self.damage_color_timer = 0.0
        self.damage_color_timeout = 0.2
        self.showing_damage = False

    def update_animations(self, dt, keys, state):
        if self.facing == 'right':
            self.play_animation('walkRight')
        elif self.facing == 'left':
            self.play_animation('walkLeft')

    def take_damage(self, damage):
        self.hp -= damage
        self.set_color([255, 0, 0])
        self.damage_color_timer = self.damage_color_timeout
        self.showing_damage = True
        if self.hp <= 0:
            self.dead = True

    def collision_callback(self, other_sprite):
        if other_sprite.is_player:
            other_sprite.take_damage(self.damage)

    def update(self, dt, keys, state):
        if self.showing_damage:
            self.damage_color_timer -= dt
            if self.damage_color_timer <= 0:
                self.set_color([255, 255, 255])
                self.showing_damage = False
        Sprite.update(self, dt, keys, state)

    def shoot(self, direction):
        self.state.sprites.append(EnemyMissile(self.x, self.y, direction, self.state))

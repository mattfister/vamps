from freezegame.sprite import Sprite
import pyglet
from vamps.player_missile import PlayerMissile


class Player(Sprite):
    def __init__(self, x, y, state):
        Sprite.__init__(self, x, y, [8, 0, 16, 30], state, 'sprites', [0, 32, 32, 32], state.batch, state.player_group)
        self.start_jump = False;
        self.jump_timeout = 0.2
        self.jump_timer = 0.0
        self.shoot_timeout = 0.5
        self.shoot_timer = 0.0
        self.jump_space_up = True
        self.double_jump_power = True
        self.double_jump_space_up = False
        self.double_jump_available = False
        self.is_player = True
        self.hp = 5
        self.create_animations()
        self.damage_timer = 0.0
        self.damage_timeout = 0.5
        self.flash_timer = 0.0
        self.flash_timeout = 0.1
        self.flash_on = False

    def create_animations(self):
        self.add_animation('standRight', [[0, 32, 32, 32], [32, 32, 32, 32]], fps=5.0)
        self.add_animation('standLeft', [[0, 64, 32, 32], [32, 64, 32, 32]], fps=5.0)
        self.add_animation('walkRight', [[64, 32, 32, 32], [96, 32, 32, 32]], fps=10.0)
        self.add_animation('walkLeft', [[64, 64, 32, 32], [96, 64, 32, 32]], fps=10.0)
        self.add_animation('jumpRight', [[128, 32, 32, 32]])
        self.add_animation('jumpLeft', [[128, 64, 32, 32]])

    def update(self, dt, keys, state):
        acc = 1000.0
        jump = 300.0

        self.jump_timer -= dt
        if self.jump_timer <= 0.0:
            self.jump_timer = 0.0

        if not self.on_ground and self.double_jump_power and self.double_jump_available and not keys[pyglet.window.key.SPACE]:
            self.double_jump_space_up = True

        if self.jump_space_up and self.on_ground and keys[pyglet.window.key.SPACE] and self.jump_timer <= 0:
            self.start_jump = True
            self.double_jump_space_up = False
            self.vy = jump
            self.jump_timer = self.jump_timeout
            self.jump_space_up = False
        elif keys[pyglet.window.key.SPACE] and self.double_jump_space_up and self.double_jump_power and self.double_jump_available and self.jump_timer <= 0:
            self.double_jump_available = False
            self.vy = jump
            self.jump_timer = self.jump_timeout

        if self.on_ground:
            self.double_jump_available = True
            if not keys[pyglet.window.key.SPACE]:
                self.jump_space_up = True

        if keys[pyglet.window.key.A]:
            self.vx += -acc * dt

        if keys[pyglet.window.key.D]:
            self.vx += acc * dt

        self.shoot_timer -= dt
        if keys[pyglet.window.key.LEFT] or keys[pyglet.window.key.RIGHT] or keys[pyglet.window.key.UP] or keys[pyglet.window.key.DOWN]:
            if keys[pyglet.window.key.LEFT]:
                self.shoot('left')
            elif keys[pyglet.window.key.RIGHT]:
                self.shoot('right')
            elif keys[pyglet.window.key.DOWN]:
                self.shoot('down')
            elif keys[pyglet.window.key.UP]:
                self.shoot('up')

        if self.damage_timer > 0.0:
            self.damage_timer -= dt
            self.flash_timer -= dt
            if self.flash_timer <= 0:
                self.flash_timer = self.flash_timeout
                if self.flash_on:
                    self.set_color([50, 50, 50])
                    self.flash_on = False
                else:
                    self.set_color([255, 255, 255])
                    self.flash_on = True
        else:
            self.set_color([255, 255, 255])



        Sprite.update(self, dt, keys, state)

    def shoot(self, direction):
        if self.shoot_timer <= 0.0:
            self.shoot_timer = self.shoot_timeout
            self.state.sprites.append(PlayerMissile(self.x, self.y, direction, self.state))


    def update_animations(self, dt, keys, state):
        if keys[pyglet.window.key.D] and self.on_ground:
            self.play_animation('walkRight')
        elif keys[pyglet.window.key.A] and self.on_ground:
            self.play_animation('walkLeft')
        elif self.on_ground and self.vx >= 0 and self.vx < 10:
            self.play_animation('standRight')
        elif self.on_ground and self.vx <0 and self.vx > -10:
            self.play_animation('standLeft')
        elif (not self.on_ground) and self.vx > 0:
            self.play_animation('jumpRight')
        elif (not self.on_ground) and self.vx < 0:
            self.play_animation('jumpLeft')

    def collision_callback(self, other_sprite):
        pass

    def take_damage(self, damage):
        if self.damage_timer <= 0:
            print('ouch ' + str(damage))
            self.damage_timer = self.damage_timeout
            self.hp -= damage
            if self.hp <= 0:
                self.dead = True

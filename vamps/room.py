import itertools
import random
import pyglet
from pyglet.gl import *
from freezegame.abstract_state import AbstractState
from freezegame.broad_phase_collision import RDC
from freezegame.tile_map import TileMap
from vamps.door import Door
from vamps.jumper import Jumper
from vamps.player import Player
from vamps.roamer import Roamer


class Room(AbstractState):
    def __init__(self, x, y, width, height, bg_data, walls_data, objects):
        AbstractState.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.batch = pyglet.graphics.Batch()
        self.player_group = pyglet.graphics.OrderedGroup(3)
        self.sprite_group = pyglet.graphics.OrderedGroup(2)
        self.wall_map_group = pyglet.graphics.OrderedGroup(1)
        self.background_group = pyglet.graphics.OrderedGroup(0)

        self.sprites = []
        self.doors = []

        self.player = None
        self.player_on_open_door = False

        self.wall_map = TileMap(32, 32,  self.width, self.height, self, 'tileSet', [0, 192, 32, 32], self.wall_map_group)

        for j in range(self.height):
            for i in range(self.width):
                if j == 0 and (i < self.width / 2 - 2 or i > self.width / 2 + 2):
                    self.wall_map.make_tile(i, j)
                if j % 4 == 0:
                    if j % 8 == 0 and j != 0 and i > 3:
                        if random.random() < 0.9:
                            self.wall_map.make_tile(i, j)
                    elif j % 8 == 4 and j != 0 and i < self.width - 3:
                        if random.random() < 0.9:
                            self.wall_map.make_tile(i, j)
                if i == 0 or i == self.width - 1:
                    self.wall_map.make_tile(i, j)
                if j == self.height - 2 and i % 10 == 0:
                    self.sprites.append(Roamer(i*32, j*32, random.choice(['left', 'right']), self))

        door = Door(5*32, 5*32, self)
        self.sprites.append(door)
        self.doors.append(door)

        self.wall_map.auto_tile()

        self.camera = [0, 0]

        self.player = Player(64, 64, self)
        self.sprites.append(self.player)



    def remove_dead_sprites(self):
        new_sprites = []
        for sprite in self.sprites:
            if sprite.dead:
                sprite.delete()
            else:
                new_sprites.append(sprite)
        self.sprites = new_sprites

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
                sprite.resolve_tile_map_collisions(self.wall_map)

        # Broad phase collision
        rdc = RDC()
        rdc.recursive_clustering(self.sprites, 0, 1)
        groups = rdc.colliding_groups

        #Now do narrow phase collision and resolution
        for group in groups:
            pairs = list(itertools.combinations(group, 2))
            for pair in pairs:
                pair[0].separate(pair[1])

        #Double check that no one resolved into a wall
        for sprite in self.sprites:
            sprite.resolve_tile_map_collisions(self.wall_map)
            if sprite.y + sprite.box[0] < 0:
                sprite.y = self.height*32
            if sprite.x + sprite.box[0] < 0:
                sprite.x = self.width*32 - sprite.box[0] - sprite.box[2]
            if sprite.x + sprite.box[0] + sprite.box[2] > self.width * 32:
                sprite.x = 0
            sprite.update_sprite_pos()

        self.remove_dead_sprites()

        any_enemies_left = False
        for sprite in self.sprites:
            if sprite.is_enemy:
                any_enemies_left = True
                break

        if not any_enemies_left:
            for door in self.doors:
                door.open()




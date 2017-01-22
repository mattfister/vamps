import random

from vamps.door import Door
from vamps.player import Player
from vamps.enemies.roamer import Roamer
from vamps.room_builders.room_builder import RoomBuilder


class ZigZag(RoomBuilder):

    def build_structure(self):
        for j in range(self.room.height):
            for i in range(self.room.width):
                if j == 0 and (i < self.room.width / 2 - 2 or i > self.room.width / 2 + 2):
                    self.room.wall_map.make_tile(i, j)
                if j % 4 == 0:
                    if j % 8 == 0 and j != 0 and i > 3:
                        if random.random() < 0.9:
                            self.room.wall_map.make_tile(i, j)
                    elif j % 8 == 4 and j != 0 and i < self.room.width - 3:
                        if random.random() < 0.9:
                            self.room.wall_map.make_tile(i, j)
                if i == 0 or i == self.room.width - 1:
                    self.room.wall_map.make_tile(i, j)

    def place_enemies(self):
        for j in range(self.room.height):
            for i in range(self.room.width):
                if j == self.room.height - 2 and i % 10 == 0:
                    self.room.sprites.append(Roamer(i*32, j*32, random.choice(['left', 'right']), self.room))

    def place_doors(self):
        door = Door(5*32, 5*32, self.room)
        self.room.sprites.append(door)
        self.room.doors.append(door)

    def place_player(self):
        self.room.player = Player(64, 64, self.room)
        self.room.sprites.append(self.room.player)




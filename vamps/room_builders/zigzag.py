import random

from vamps.door import Door
from vamps.enemies.blaster import Blaster
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
                            self.room.enemy_spots.append([i, j+1])
                            self.room.door_spots.append([i, j+1])
                    elif j % 8 == 4 and j != 0 and i < self.room.width - 3:
                        if random.random() < 0.9:
                            self.room.wall_map.make_tile(i, j)
                            self.room.enemy_spots.append([i, j+1])
                            self.room.door_spots.append([i, j+1])
                if i == 0 or i == self.room.width - 1:
                    self.room.wall_map.make_tile(i, j)

    def place_player(self):
        self.room.player = Player(64, 64, self.room)
        self.room.sprites.append(self.room.player)

import random

from vamps.player import Player
from vamps.room_builders.room_builder import RoomBuilder


class Pit(RoomBuilder):

    def build_structure(self):
        for j in range(self.room.height):
            for i in range(self.room.width):
                if j == 0:
                    self.room.wall_map.make_tile(i, j)
                if i == 0 or i == self.room.width - 1:
                    self.room.wall_map.make_tile(i, j)
                if j > 5 and j < 20 and i > 0 and i < self.room.width - 1:
                    self.room.air_enemy_spots.append([i, j])
                if j == 1 and i > 0 and i < self.room.width - 1:
                    self.room.door_spots.append([i, j])
                    self.room.player_spots.append([i, j+1])

import random

from vamps.player import Player
from vamps.room_builders.room_builder import RoomBuilder


class ZigZag(RoomBuilder):

    def build_structure(self):

        gap_size = random.randint(1, 3)
        floor_height = random.randint(4, 6)
        for j in range(self.room.height):
            for i in range(self.room.width):
                if j == 0 and (i < self.room.width / 2 - 2 or i > self.room.width / 2 + 2) and i > 0 and i < self.room.width-1:
                    self.room.wall_map.make_tile(i, j)
                    self.room.player_spots.append([i, j+1])
                if j % floor_height == 0:
                    if j % (floor_height*2) == 0 and j != 0 and i > 3:
                        self.room.wall_map.make_tile(i, j)
                        self.room.ground_enemy_spots.append([i, j+1])
                        #self.room.air_enemy_spots.append([i, j+2])
                        #self.room.air_enemy_spots.append([i, j+3])
                        self.room.door_spots.append([i, j+1])
                    elif j % (floor_height*2) == floor_height and j != 0 and i < self.room.width - 3:
                        self.room.wall_map.make_tile(i, j)
                        self.room.ground_enemy_spots.append([i, j+1])
                        #self.room.air_enemy_spots.append([i, j+2])
                        #self.room.air_enemy_spots.append([i, j+3])
                        self.room.door_spots.append([i, j+1])
                if i == 0 or i == self.room.width - 1:
                    self.room.wall_map.make_tile(i, j)


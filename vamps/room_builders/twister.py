import random
import math

from vamps.player import Player
from vamps.room_builders.room_builder import RoomBuilder


class Twister(RoomBuilder):

    def build_structure(self):

        gap = random.randint(0, self.room.width)
        twist = random.randint(-5, 5)
        gap_size = random.randint(1,3)
        floor_height = random.randint(3, 5)
        for j in range(self.room.height):
            gap += twist
            if gap > self.room.width - 1:
                gap %= self.room.width - 1
            if gap < 0:
                gap += self.room.width - 1
            for i in range(self.room.width):
                gap_dist = abs(i - gap)
                if j == 0 and gap_dist > gap_size:
                    self.room.wall_map.make_tile(i, j)
                    self.room.player_spots.append([i, j+1])
                if j % floor_height == 0:
                    if j != 0 and gap_dist > gap_size:
                        self.room.wall_map.make_tile(i, j)
                        self.room.ground_enemy_spots.append([i, j+1])
                        self.room.door_spots.append([i, j+1])

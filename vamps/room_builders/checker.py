import random

from vamps.room_builders.room_builder import RoomBuilder


class Checker(RoomBuilder):

    def build_structure(self):
        x_space = random.randint(3, 7)
        y_space = random.randint(3, 4)
        x_offset = 0
        for j in range(self.room.height):
            x_offset += 1
            for i in range(self.room.width):
                if i > 0 and i < self.room.width - 1 and j > 3:
                    if (i + x_offset) % x_space == 0 and j % y_space == 0:
                        self.room.wall_map.make_tile(i, j)
                        self.room.ground_enemy_spots.append([i, j+1])
                if j == 0 and (i % x_space != 0):
                    self.room.wall_map.make_tile(i, j)
                if i == 0 or i == self.room.width - 1:
                    self.room.wall_map.make_tile(i, j)
                if j == 1 and i > 0 and i < self.room.width - 1:
                    self.room.door_spots.append([i, j])
                    self.room.player_spots.append([i, j+1])

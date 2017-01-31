import random

from vamps.room_builders.room_builder import RoomBuilder


class Platforms(RoomBuilder):

    def build_structure(self):
        y_space = random.randint(3, 4)
        for j in range(self.room.height):
            x_space = random.randint(1, self.room.width - 1)
            plat_size = random.randint(5, 7)
            for i in range(self.room.width):
                if j > y_space:
                    if j % y_space == 0:
                        if i > x_space - plat_size and i < x_space + plat_size:
                            self.room.wall_map.make_tile(i, j)
                            self.room.ground_enemy_spots.append([i, j+1])
                if i == 0 or i == self.room.width - 1:
                    self.room.wall_map.make_tile(i, j)
                if j == 0 and (i < self.room.width / 2 - 2 or i > self.room.width / 2 + 2) and i > 0 and i < self.room.width-1:
                    self.room.wall_map.make_tile(i, j)
                    self.room.door_spots.append([i, j+1])
                    self.room.player_spots.append([i, j+1])

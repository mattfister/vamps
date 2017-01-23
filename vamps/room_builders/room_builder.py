import random
from vamps.door import Door
from vamps.enemies.blaster import Blaster
from vamps.enemies.eagle import Eagle
from vamps.enemies.roamer import Roamer
from vamps.enemies.seeker import Seeker
from vamps.room import Room


class RoomBuilder:
    def __init__(self, level):
        self.level = level
        self.room = Room(0, 0, 60, 32, None, None, None)

    def build_room(self):
        self.build_structure()
        self.auto_tile()
        print(self.room.enemy_spots)
        random.shuffle(self.room.enemy_spots)
        self.place_enemies()
        self.place_doors()
        self.place_player()
        return self.room

    def build_structure(self):
        pass

    def auto_tile(self):
        self.room.wall_map.auto_tile()

    def place_enemies(self):
        enemies_to_place = 5
        while enemies_to_place > 0:
            spot = self.room.enemy_spots.pop(0)
            enemy_class = random.choice(self.get_enemy_classes())
            self.room.sprites.append(enemy_class(spot[0]*32, spot[1]*32, random.choice(['left', 'right']), self.room))
            enemies_to_place -= 1

    def place_doors(self):
        spot = random.choice(self.room.door_spots)
        door = Door(spot[0]*32, spot[1]*32, self.room)
        self.room.sprites.append(door)
        self.room.doors.append(door)


    def place_player(self):
        pass

    def get_enemy_classes(self):
        return [Blaster, Roamer, Eagle, Seeker]
import random
from vamps.door import Door
from vamps.enemies.blaster import Blaster
from vamps.enemies.eagle import Eagle
from vamps.enemies.roamer import Roamer
from vamps.enemies.seeker import Seeker
from vamps.enemies.seeking_eagle import SeekingEagle
from vamps.enemies.smart_hopper import Hopper
from vamps.enemies.sniper import Sniper
from vamps.enemies.turret import Turret
from vamps.player import Player
from vamps.room import Room


class RoomBuilder:
    def __init__(self, level):
        self.level = level
        self.room = Room(0, 0, 60, 32, None, None, None)

    def build_room(self):
        self.build_structure()
        self.auto_tile()
        random.shuffle(self.room.ground_enemy_spots)
        random.shuffle(self.room.air_enemy_spots)
        self.place_enemies()
        self.place_doors()
        self.place_player()
        return self.room

    def build_structure(self):
        pass

    def auto_tile(self):
        self.room.wall_map.auto_tile()

    def place_enemies(self):
        total_enemy_types = random.randint(1, 3)
        num_air_enemy_types = random.randint(0, total_enemy_types)
        if len(self.room.air_enemy_spots) == 0:
            num_air_enemy_types = 0
        num_ground_enemy_types = total_enemy_types - num_air_enemy_types
        if len(self.room.ground_enemy_spots) == 0:
            num_ground_enemy_types = 0
            num_air_enemy_types = total_enemy_types
        air_enemies = random.sample(self.get_air_enemy_classes(), num_air_enemy_types)
        ground_enemies = random.sample(self.get_ground_enemy_classes(), num_ground_enemy_types)
        enemies_to_place = 5
        while enemies_to_place > 0:
            place_air_enemy = random.randint(0, total_enemy_types-1) < num_air_enemy_types
            if place_air_enemy:
                spot = self.room.air_enemy_spots.pop(0)
                enemy_class = random.choice(air_enemies)
            else:
                spot = self.room.ground_enemy_spots.pop(0)
                enemy_class = random.choice(ground_enemies)
            self.room.sprites.append(enemy_class(spot[0]*32, spot[1]*32, random.choice(['left', 'right']), self.room))
            enemies_to_place -= 1

    def place_doors(self):
        spot = random.choice(self.room.door_spots)
        door = Door(spot[0]*32, spot[1]*32, self.room)
        self.room.sprites.append(door)
        self.room.doors.append(door)

    def place_player(self):
        spot = random.choice(self.room.player_spots)
        self.room.player = Player(spot[0]*32, spot[1]*32 , self.room)
        self.room.sprites.append(self.room.player)

    def get_ground_enemy_classes(self):
        return [Blaster, Roamer, Seeker, Sniper, Hopper]

    def get_air_enemy_classes(self):
        return [Eagle, Turret, SeekingEagle]

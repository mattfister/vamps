from vamps.room import Room


class RoomBuilder:
    def __init__(self, level):
        self.level = level
        self.room = Room(0, 0, 60, 32, None, None, None)

    def build_room(self):
        self.build_structure()
        self.auto_tile()
        self.place_enemies()
        self.place_doors()
        self.place_player()
        return self.room

    def build_structure(self):
        pass

    def auto_tile(self):
        self.room.wall_map.auto_tile()

    def place_enemies(self):
        pass

    def place_doors(self):
        pass

    def place_player(self):
        pass
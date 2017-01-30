import random
from vamps.room_builders.pit import Pit
from vamps.room_builders.twister import Twister
from vamps.room_builders.zigzag import ZigZag


def build_room(level):
    rooms = [ZigZag, Pit, Twister]
    #rooms = [ZigZag]
    room = random.choice(rooms)
    room_builder = room(level)
    return room_builder.build_room()

import random

from vamps.room_builders.checker import Checker
from vamps.room_builders.pit import Pit
from vamps.room_builders.platforms import Platforms
from vamps.room_builders.twister import Twister
from vamps.room_builders.zigzag import ZigZag


def build_room(level, old_player):
    rooms = [ZigZag, Pit, Twister, Platforms, Checker]
    room = random.choice(rooms)
    room_builder = room(level)
    return room_builder.build_room(old_player)

from vamps.room import Room
from vamps.room_builders.room_builder import RoomBuilder
from vamps.room_builders.zigzag import ZigZag


def build_room(level):
    room_builder = ZigZag(level)
    return room_builder.build_room()

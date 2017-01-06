import json


class RoomData():
    def __init__(self, path):
        file = open(path)
        self.__dict__ = json.load(file)

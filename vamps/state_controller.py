import pyglet

from freezegame.abstract_state import AbstractState
from vamps.room import Room


class StateController(AbstractState):
    def __init__(self):
        self.current_state = Room(0, 0, 60, 32, None, None, None)

    def update(self, dt, keys):
        self.current_state.update(dt, keys)
        if self.current_state.player_on_open_door:
            self.current_state = Room(0, 0, 60, 32, None, None, None)

    def draw(self):
        self.current_state.draw()

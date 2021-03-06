import pyglet

from freezegame.abstract_state import AbstractState
import vamps.room_builders.room_factory
import vamps.constants

class StateController(AbstractState):
    def __init__(self):
        self.level = 1
        self.current_state = vamps.room_builders.room_factory.build_room(self.level, None)

    def update(self, dt, keys):
        self.current_state.update(dt, keys)
        if self.current_state.player_on_open_door or (vamps.constants.DEBUG and keys[pyglet.window.key._1]):
            next_room = vamps.room_builders.room_factory.build_room(self.level, self.current_state.player)
            self.level += 1
            self.current_state = next_room

    def draw(self):
        self.current_state.draw()

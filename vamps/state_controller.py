from freezegame.abstract_state import AbstractState
import vamps.room_builders.room_factory


class StateController(AbstractState):
    def __init__(self):
        self.level = 1
        self.current_state = vamps.room_builders.room_factory.build_room(self.level)

    def update(self, dt, keys):
        self.current_state.update(dt, keys)
        if self.current_state.player_on_open_door:
            next_room = vamps.room_builders.room_factory.build_room(self.level)
            self.level += 1
            self.current_state = next_room

    def draw(self):
        self.current_state.draw()

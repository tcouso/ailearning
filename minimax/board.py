class UsedSlotError(Exception):
    def __init__(self, coordinates, token):
        super().__init__(
            f"Slot in {coordinates} is already filled with {token} token"
        )


class Board():
    def __init__(self):
        self.__game_state = False
        self.grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def place_token(self, token, coordinates):
        try:
            x, y = coordinates
            slot = self.grid[y][x]
            if slot is not None:
                raise UsedSlotError(coordinates, token)
            self.grid[y][x] = token
        except (IndexError, UsedSlotError) as err:
            print(f'Invalid move: {err}')

    @property
    def game_state(self):
        return self.__game_state

    @game_state.setter
    def game_state(self, new_state):
        self.__game_state = new_state

    def finished_board(self):
        pass

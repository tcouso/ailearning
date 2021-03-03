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

    def check_winner(self):
        if self.win_1 or self.win_2 or self.win_3 or self.win_4:
            self.game_state = True

    def win_1(self):
        "Horizontal win."
        for i in range len(self.grid):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2]:
                return True
        return False

    def win_2(self):
        "Vertical win."
        for i in range len(self.grid):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                return True
        return False

    def win_3(self):
        "Northwest to southeast win."
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return True
        return False

    def win_4(self):
        "Southwest to northeast win."
        if self.grid[2][0] == self.grid[1][1] == self.grid[0][2]:
            return True
        return False

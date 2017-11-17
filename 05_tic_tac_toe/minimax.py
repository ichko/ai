

class Minmax:
    def __init__(self):
        self.cache = []

    def make_move(self, state):
        pass


def get_start_state():
    return []

def get_user_move(state):
    return input()

def print_state(state):
    print(state)

def solved(state):
    pass

def get_winner(state):
    return 'winner'


if __name__ == '__mani__':
    ai_strategy = Minmax()
    players = [get_user_move, ai_strategy.make_move]
    current_state = get_start_state()

    while not solved(current_state):
        current_player = players[0]
        current_state = current_player(current_state)
        players = players[1:] + players[:1]

    print(players[-1])

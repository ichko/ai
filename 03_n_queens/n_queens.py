import defaultdict


class NQueen:

    def __init__(self, problem_size):
        self.problem_size = problem_size
        self.conflicts = defaultdict(lambda: 0)
        self.board = []

        self.genarate_initial_board()
        self.calculate_conflicts()

    def genarate_initial_board(self):
        self.board = [i for i in range(self.problem_size)]

    def calculate_conflicts(self):
        for y in self.problem_size:
            pass
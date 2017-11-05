from collections import defaultdict
import random


def argmin(arr):
    min_id = 0
    for id, el in enumerate(arr):
        if arr[min_id]> el: min_id = id
    return min_id


class Column:

    def __init__(self, problem_size):
        self.problem_size = problem_size
        self.queen_position = 1
        self.conflicts = [0 for _ in range(problem_size)]

    def is_solved(self):
        return self.conflicts[self.queen_position] == 0

    def relocate_queen(self):
        min_id = argmin(self.conflicts)
        old_queen_position = self.queen_position
        self.queen_position = min_id
        return min_id != old_queen_position

    def update_conflict(self, y, value=1):
        self.conflicts[y] += value

    def get_conflicting_cells(self):
        result = [(x, self.queen_position)
                  for x in range(self.problem_size)]

        return result


class NQueen:

    def __init__(self, problem_size):
        self.problem_size = problem_size
        self.board = [Column(problem_size)
                      for _ in range(problem_size)]
        self.set_inital_conflicts()

    def is_solved(self):
        return all(c.is_solved() for c in self.board)

    def solve(self, max_iter=1000):
        while max_iter > 0:
            if not self.is_solved():
                max_iter -= 1
                x = random.randrange(0, len(self.board))
                old_conflicts = self.board[x].get_conflicting_cells()
                if self.board[x].relocate_queen():
                    new_conflicts = self.board[x].get_conflicting_cells()
                    self.update_conflicts(old_conflicts, new_conflicts)
            else:
                return self.construct_solution()
        return self.construct_solution()

    def construct_solution(self):
        return set((x, col.queen_position)
                   for x, col in enumerate(self.board))

    def update_conflicts(self, old_conflicts, new_conflicts):
        for x, y in old_conflicts:
            self.board[x].update_conflict(y, -1)
        for x, y in new_conflicts:
            self.board[x].update_conflict(y, 1)

    def set_inital_conflicts(self):
        for col in self.board:
            conflicting_cells = col.get_conflicting_cells()
            for x, y in conflicting_cells:
                self.board[x].update_conflict(y, 1)



def print_solution(solution, problem_size):
    for y in range(problem_size):
        for x in range(problem_size):
            print('Q' if (x, y) in solution else '-', end='')
        print()


if __name__ == '__main__':
    problem_size = int(input())
    game = NQueen(problem_size)
    solution = game.solve()
    print_solution(solution, problem_size)
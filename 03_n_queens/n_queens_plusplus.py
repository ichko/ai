from collections import defaultdict
from random import randrange as rand


def solve(n):
    return NQueens(n).solve()
    
def is_solved(solution):
    return solution.is_solved()


class NQueens:

    def __init__(self, n):
        self.n = n
        self._init_q()

    def solve(self):
        max_iter = self.n * 2.71 # MAGIC
        current_iter = max_iter
        while True:
            if current_iter <= 0:
                current_iter = max_iter
                self._init_q()
            if self.is_solved():
                return self
            else:
                q_max = max(self.queens, key=lambda q: self.conflicts[q])
                q_new = self._get_new_q(q_max)
                self._move_q(q_max, q_new)

    def is_solved(self):
        return all(self.conflicts[q] == 1 for q in self.queens)

    def _get_new_q(self, q_pos):
        x, _ = q_pos
        return min([(x, y) for y in range(self.n)],
                   key=lambda q: self.conflicts[q])

    def _init_q(self):
        self.conflicts = defaultdict(lambda: 0)
        self.queens = set()

        for x in range(self.n):
            q_pos = (x, rand(0, self.n))
            self.queens.add(q_pos)
            for pos in self._get_q_conflicts(q_pos):
                self.conflicts[pos] += 1

    def _move_q(self, q_old, q_new):
        for pos in self._get_q_conflicts(q_old):
            self.conflicts[pos] -= 1
        for pos in self._get_q_conflicts(q_new):
            self.conflicts[pos] += 1

    def _get_q_conflicts(self, q_pos):
        qx, qy = q_pos
        result = set((x, qy) for x in range(self.n))
        result.update((qx, y) for y in range(self.n))

        min_coord, max_coord = min(qx, qy), max(qx, qy)
        min_inv, max_inv = min(self.n - qx - 1, qy), max(self.n - qx - 1, qy)

        x_base, y_base = qx - min_coord, qy - min_coord
        x_inv, y_inv = qx + min_inv, qy - min_inv

        result.update((x_base + i, y_base + i)
            for i in range(self.n - (max_coord - min_coord)))
        result.update((x_inv - i, y_inv + i)
            for i in range(self.n - (max_inv - min_inv)))

        return result

    def print_board(self):
        for y in range(self.n):
            print(' '.join(['*' if (x, y) in self.queens else '.'
                           for x in range(self.n)]))


if __name__ == '__main__':
    n = int(input())
    solve(n).print_board()

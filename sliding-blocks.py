from queue import PriorityQueue as p_queue
import unittest
from collections import defaultdict


class Graph:

    def get_children(self, vertex):
        raise NotImplementedError()

    def heuristic(self, current, goal):
        return 0

    @staticmethod
    def get_path(start, end, predecessor):
        current = end
        while current != start:
            yield current
            current = predecessor[current]

    def a_star(self, start, end):
        predecessor = {}
        distance = defaultdict(lambda: float('inf'))
        distance[start] = 0
        visited = set()
        front = p_queue()
        front.put(start, 0)

        while not front.empty():
            current = front.get()
            visited.add(current)

            if current == end:
                return Graph.get_path(start, end, predecessor)

            for child, weight in self.get_children(current):
                new_dist = distance[current] + weight
                if child not in visited and distance[child] > new_dist:
                    distance[child] = new_dist
                    predecessor[child] = current
                    heuristic = distance[child] + self.heuristic(current, end)
                    front.put(child, heuristic)

        return []


class SlidingBlocksGraph(Graph):

    def __init__(self, start):
        self.start = tuple(tuple(el for el in row) for row in start)
        cols, rows = self.get_board_shape(start)
        self.cols = cols
        self.rows = rows
        self.end = self.get_board_end(cols, rows)
        self.zero_pos_x, self.zero_pos_y = self.get_zero_pos(self.end)

    def solve(self):
        solution_path = list(self.a_star(self.start, self.end))
        solution = self.convet_path_to_moves(solution_path)
        return list(solution)

    def get_board_shape(self, board):
        return len(board[0]), len(board)

    def get_board_end(self, cols, rows):
        size = cols * rows
        return tuple(tuple(((r * rows) + c + 1) % size for c in range(cols))
                                                       for r in range(rows))

    def convet_path_to_moves(self, solution_path):
        for src, dst in zip(solution_path, solution_path[1:]):
            yield self.get_move_between_boards(src, dst)

    def get_children(self, state):
        result = []
        x, y = self.get_zero_pos(state)

        if y > 0: result.append(self.swap(state, x, y, x, y - 1))
        if y < self.rows - 1: result.append(self.swap(state, x, y, x, y + 1))
        if x > 0: result.append(self.swap(state, x, y, x - 1, y))
        if x < self.cols - 1: result.append(self.swap(state, x, y, x + 1, y))

        return result

    def swap(self, state, src_x, src_y, dst_x, dst_y):
        new_state = [[el for el in row] for row in state]
        tmp = new_state[src_y][src_x];
        new_state[src_y][src_x] = new_state[dst_y][dst_x]
        new_state[dst_y][dst_x] = tmp

        return tuple(tuple(el for el in row) for row in new_state), 1

    def heuristic(self, current, goal):
        return 0

    def get_move_between_boards(self, src, dst):
        src_zero_x, src_zero_y = self.get_zero_pos(src)
        dst_zero_x, dst_zero_y = self.get_zero_pos(dst)
        dx, dy = src_zero_x - dst_zero_x, src_zero_y - dst_zero_y
        if dy == 1: return 'up'
        if dy == -1: return 'down'
        if dx == 1: return 'left'
        if dx == -1: return 'right'

    def get_zero_pos(self, state):
        for y_pos in range(len(state)):
            if 0 in state[y_pos]:
                return state[y_pos].index(0), y_pos
        return -1, -1


class SlidingBlocksTests(unittest.TestCase):

    def test_single_square_solved_board(self):
        self.assertEqual(SlidingBlocksGraph([[0]]).solve(), [])

    def test_single_square_unsolvable_board(self):
        self.assertEqual(SlidingBlocksGraph([[1]]).solve(), [])

    def test_four_square_solved_board(self):
        self.assertEqual(SlidingBlocksGraph([
            [1, 2],
            [3, 0]
        ]).solve(), [])

    def test_four_square_unsolvable_board(self):
        self.assertEqual(SlidingBlocksGraph([
            [3, 2], 
            [1, 0]
        ]).solve(), [])

    def test_four_square_complex_board(self):
        self.assertEqual(SlidingBlocksGraph([
            [2, 3], 
            [1, 0]
        ]).solve(), ['down', 'right', 'up', 'left'])

    def test_single_row_board(self):
        self.assertEqual(SlidingBlocksGraph([
            [0, 1, 2, 3]
        ]).solve(), ['left', 'left', 'left'])

    def test_single_col_board(self):
        self.assertEqual(SlidingBlocksGraph([
            [0],
            [1],
            [2],
            [3]
        ]).solve(), ['up', 'up', 'up'])

    def test_rectangle_board(self):
        self.assertEqual(SlidingBlocksGraph([
            [1, 2, 3],
            [0, 4, 5]
        ]).solve(), ['left', 'left'])

    def test_example_board(self):
        self.assertEqual(SlidingBlocksGraph([
            [1, 2, 3],
            [4, 5, 6],
            [0, 7, 8]
        ]).solve(), ['left', 'left'])

    def test_complex_board(self):
        # TODO: Think of complex example
        # self.assertEqual(SlidingBlocksGraph([
        #     [1, 2, 3]
        # ]).solve(), [])
        pass

    def test_big_complex_board(self):
        # TODO: Think of complex example
        # self.assertEqual(SlidingBlocksGraph([
        #     [1, 2, 3]
        # ]).solve(), [])
        pass


if __name__ == '__main__':
    unittest.main()

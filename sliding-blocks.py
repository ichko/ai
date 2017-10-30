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
        front.put(0, start)

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
                    front.put(heuristic, child)


class SlidingBlocksGraph(Graph):

    def __init__(self, start):
        self.start = tuple(tuple(el for el in row) for row in start)
        cols, rows = self.get_board_shape(start)
        self.end = self.get_board_end(cols, rows)

    def solve(self):
        solution_path = self.a_star(self.start, self.end)
        solution = self.convet_path_to_moves(solution_path)
        return list(solution)

    def get_board_shape(self, board):
        return len(board[0]), len(board)

    def get_board_end(self, cols, rows):
        size = cols * rows
        return tuple(tuple((r * c) % size for c in range(cols))
                                          for r in range(rows))

    def convet_path_to_moves(self, solution_path):
        for src, dst in zip(solution_path, solution_path[1:]):
            yield self.get_move_between_boards(src, dst)

    def get_children(self, vertex):
        pass

    def heuristic(self, current, goal):
        pass

    def get_move_between_boards(self, src, dst):
        pass


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
        self.assertEqual(SlidingBlocksGraph([
            [1, 2, 3]
        ]).solve(), [])

    def test_big_complex_board(self):
        # TODO: Think of complex example
        self.assertEqual(SlidingBlocksGraph([
            [1, 2, 3]
        ]).solve(), [])


if __name__ == '__main__':
    unittest.main()
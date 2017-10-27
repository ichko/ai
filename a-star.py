import unittest
from collections import defaultdict


class Graph:

    def get_children(self, vertex):
        pass

    def a_star(self, start, end):
        distance = defaultdict(lambda: float('inf'))
        distance[start] = 0
        unvisited = set(self.vertices)
        current = start

        while len(self.adjacencies[current]) != 0 and len(unvisited) != 0:
            for child, weight in self.get_children(current):
                distance[child] = min(
                    distance[child],
                    distance[current] + weight
                )
            unvisited.remove(current)
            if current == end:
                return distance[current]


class SlidingBlocksGraph(Graph):

    def solve(self, start):
        cols, rows = self.get_board_shape(start)
        end = self.get_board_end(cols, rows)
        solution_path = self.a_star(start, end)
        solution = self.convet_path_to_moves(solution_path)
        return list(solution)

    def get_board_shape(self, board):
        return len(board[0]), len(board)

    def get_board_end(self, cols, rows):
        size = cols * rows
        return [[(r * c) % size for c in range(cols)] for r in range(rows)]

    def convet_path_to_moves(self, solution_path):
        for src, dst in zip(solution_path, solution_path[1:]):
            yield self.get_move_between_boards(src, dst)

    def get_move_between_boards(self, srx, dst):
        pass


class AStartTests(unittest.TestCase):

    def test_single_square_solved_board(self):
        self.assertEqual(SlidingBlocksGraph().solve([[0]]), [])

    def test_single_square_unsolvable_board(self):
        self.assertEqual(SlidingBlocksGraph().solve([[1]]), [])

    def test_four_square_solved_board(self):
        self.assertEqual(SlidingBlocksGraph().solve([
            [1, 2],
            [3, 0]
        ]), [])

    def test_four_square_unsolvable_board(self):
        self.assertEqual(SlidingBlocksGraph().solve([
            [3, 2], 
            [1, 0]
        ]), [])

    def test_four_square_complex_board(self):
        self.assertEqual(SlidingBlocksGraph().solve([
            [2, 3], 
            [1, 0]
        ]), ['down', 'right', 'up', 'left'])

    def test_single_row_board(self):
        self.assertEqual(SlidingBlocksGraph().solve([
            [0, 1, 2, 3]
        ]), ['left', 'left', 'left'])

    def test_single_col_board(self):
        self.assertEqual(SlidingBlocksGraph().solve([
            [[0],
             [1],
             [2],
             [3]]
        ]), ['up', 'up', 'up'])

    def test_rectangle_board(self):
        self.assertEqual(SlidingBlocksGraph().solve([
            [1, 2, 3],
            [0, 4, 5]
        ]), ['left', 'left'])

    def test_example_board(self):
        self.assertEqual(SlidingBlocksGraph().solve([
            [1, 2, 3],
            [4, 5, 6],
            [0, 7, 8]
        ]), ['left', 'left'])

    def test_complex_example_board(self):
        # TODO: Think of complex example
        self.assertEqual(SlidingBlocksGraph().solve([
            [1, 2, 3]
        ]), [])

    def test_big_board_complex_example(self):
        # TODO: Think of complex example
        self.assertEqual(SlidingBlocksGraph().solve([
            [1, 2, 3]
        ]), [])


if __name__ == '__main__':
    unittest.main()

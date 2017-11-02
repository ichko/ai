import unittest
from sliding_blocks import SlidingBlocksGraph


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

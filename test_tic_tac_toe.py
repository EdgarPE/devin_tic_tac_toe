import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_board_initialization(self):
        self.assertEqual(self.game.board, [' ' for _ in range(9)])
        self.assertEqual(self.game.current_player, 'X')

    def test_make_move(self):
        self.assertTrue(self.game.make_move(0))
        self.assertEqual(self.game.board[0], 'X')
        self.assertEqual(self.game.current_player, 'O')

        self.assertFalse(self.game.make_move(0))  # Already occupied
        self.assertEqual(self.game.board[0], 'X')
        self.assertEqual(self.game.current_player, 'O')

    def test_check_winner_rows(self):
        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(self.game.check_winner(), 'X')

    def test_check_winner_columns(self):
        self.game.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
        self.assertEqual(self.game.check_winner(), 'O')

    def test_check_winner_diagonals(self):
        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertEqual(self.game.check_winner(), 'X')

    def test_check_tie(self):
        self.game.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertEqual(self.game.check_winner(), 'Tie')

    def test_game_in_progress(self):
        self.game.board = ['X', 'O', 'X', ' ', 'O', ' ', ' ', ' ', ' ']
        self.assertIsNone(self.game.check_winner())

if __name__ == '__main__':
    unittest.main()

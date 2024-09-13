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

    def test_full_game_x_wins(self):
        moves = [0, 1, 3, 4, 6]  # X's moves to win
        for i, move in enumerate(moves):
            self.game.make_move(move)
            if i < len(moves) - 1:
                self.assertIsNone(self.game.check_winner())
            else:
                self.assertEqual(self.game.check_winner(), 'X')

    def test_full_game_o_wins(self):
        moves = [0, 4, 1, 2, 3, 6]  # Alternating moves, O wins
        for i, move in enumerate(moves):
            self.game.make_move(move)
            if i < len(moves) - 1:
                self.assertIsNone(self.game.check_winner())
            else:
                self.assertEqual(self.game.check_winner(), 'O')

    def test_invalid_move_occupied_space(self):
        self.game.make_move(0)  # X moves to position 0
        self.assertFalse(self.game.make_move(0))  # Try to move to the same position
        self.assertEqual(self.game.board[0], 'X')  # The position should still be 'X'
        self.assertEqual(self.game.current_player, 'O')  # The current player should still be 'O'

    def test_invalid_move_out_of_range(self):
        initial_board = self.game.board.copy()
        initial_player = self.game.current_player
        self.assertFalse(self.game.make_move(9))  # Try to move to an out-of-range position
        self.assertEqual(self.game.board, initial_board)  # The board should remain unchanged
        self.assertEqual(self.game.current_player, initial_player)  # The current player should remain unchanged

    def test_game_state_unchanged_after_invalid_move(self):
        self.game.make_move(0)  # X moves to position 0
        initial_board = self.game.board.copy()
        initial_player = self.game.current_player
        self.assertFalse(self.game.make_move(0))  # Try to move to an occupied position
        self.assertEqual(self.game.board, initial_board)  # The board should remain unchanged
        self.assertEqual(self.game.current_player, initial_player)  # The current player should remain unchanged

if __name__ == '__main__':
    unittest.main()

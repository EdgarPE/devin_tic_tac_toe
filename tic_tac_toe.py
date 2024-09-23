import random

class TicTacToe:
    def __init__(self, computer_player='X'):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_player = 'X'
        self.computer_player = computer_player
        self.human_player = 'O' if computer_player == 'X' else 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print(f'{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}')
            if i < 6:
                print('---------')

    def make_move(self, position):
        if 0 <= position <= 8 and self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        # Check rows, columns, and diagonals
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        if ' ' not in self.board:
            return 'Tie'
        return None

    def get_winning_move(self, player):
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = player
                if self.check_winner() == player:
                    self.board[i] = ' '
                    return i
                self.board[i] = ' '
        return None

    def get_computer_move(self):
        # Rule 1 & 2: If board is empty, start in the middle
        if all(cell == ' ' for cell in self.board):
            return 4

        # Rule 3: If computer can win in 1 move, make the winning move
        winning_move = self.get_winning_move(self.computer_player)
        if winning_move is not None:
            return winning_move

        # Rule 4: If player can win in 1 move, block that move
        blocking_move = self.get_winning_move(self.human_player)
        if blocking_move is not None:
            return blocking_move

        # Rule 5: Make a random valid move
        empty_cells = [i for i, cell in enumerate(self.board) if cell == ' ']
        return random.choice(empty_cells)

def play_game():
    game = TicTacToe()  # Computer is 'X' by default
    winner = None

    while not winner:
        game.print_board()

        if game.current_player == game.computer_player:
            move = game.get_computer_move()
            print(f"Computer ({game.computer_player}) chooses position {move}")
        else:
            try:
                move = int(input(f"Player ({game.human_player}), enter your move (0-8): "))
                if not (0 <= move <= 8 and game.board[move] == ' '):
                    print("Invalid move. Please choose an empty position between 0 and 8.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        if game.make_move(move):
            winner = game.check_winner()
        else:
            print("That position is already occupied. Try again.")

    game.print_board()
    if winner == 'Tie':
        print("It's a tie!")
    else:
        print(f"{'Computer' if winner == game.computer_player else 'Player'} ({winner}) wins!")

if __name__ == "__main__":
    play_game()

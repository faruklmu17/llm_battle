
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.winner = None

    def display_board(self):
        # Create a display that shows either the symbol or the index
        display = [str(i) if spot == " " else spot for i, spot in enumerate(self.board)]
        rows = [display[i:i+3] for i in range(0, 9, 3)]
        board_str = "\n"
        for i, row in enumerate(rows):
            board_str += f" {row[0]} | {row[1]} | {row[2]} "
            if i < 2:
                board_str += "\n-----------\n"
        return board_str

    def get_valid_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position):
        if self.board[position] == " " and self.winner is None:
            self.board[position] = self.current_player
            if self.check_winner(self.current_player):
                self.winner = self.current_player
            elif " " not in self.board:
                self.winner = "Draw"
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
            [0, 4, 8], [2, 4, 6]             # Diagonal
        ]
        return any(all(self.board[i] == player for i in combo) for combo in win_conditions)

    def is_game_over(self):
        return self.winner is not None

    def get_state_prompt(self):
        """Returns a string representation of the board for the LLM."""
        return (
            f"Current Tic-Tac-Toe Board:\n"
            f"{self.display_board()}\n\n"
            f"IMPORTANT: You are playing as '{self.current_player}'.\n"
            f"You MUST choose one of the available numbers on the board: {self.get_valid_moves()}\n"
            f"Your move (0-8):"
        )

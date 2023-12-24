from games import Game, GameState, query_player, alpha_beta_search, alpha_beta_player

class GameOfNim(Game):
    def __init__(self, board=[7,5,3,1]):
        # Initialize the initial state with the initial board configuration and all valid moves.

        moves = []
        for row in range(len(board)):
            for match_amount in range(1, board[row] + 1):
                moves.append((row, match_amount))

        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)

    def actions(self, state):
        # Return a list of valid actions (moves) in the given state.
        return state.moves

    def result(self, state, move):
        # Create a new state based on the given state and a valid move.
        row, num_objects = move
        new_board = list(state.board)
        new_board[row] -= num_objects

        new_moves = []
        for row in range(len(new_board)):
            for match_amount in range(1, new_board[row] + 1):
                new_moves.append((row, match_amount))

        new_to_move = ("MAX" if state.to_move == "MIN" else "MIN")
        new_utility = self.utility(GameState(to_move=new_to_move, utility=0, board=new_board, moves=new_moves), new_to_move)
        new_state = GameState(to_move=new_to_move, utility=new_utility, board=new_board, moves=new_moves)
        return new_state

    def utility(self, state, player):
        # Return the utility value for the given player.
        if state.to_move == player:
            return 1  # The player whose turn it is wins
        else:
            return -1  # The other player wins

    def terminal_test(self, state):
        # A state is terminal if there are no objects left
        return len(state.moves) == 0

    def to_move(self, state):
        return state.to_move

    def display(self, state):
        board = state.board
        print(board)

if __name__ == "__main__":
    nim = GameOfNim([7, 5, 3, 1])
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]#use a single list to rep 3*3 board
        self.current_winner = None #tracking the winner

        def print_board(self): #getting the rows
            for row in [self.board[1*3:(i*i)*3] for i in range(3)]:
                print(' | ' + ' | ' .join(row) + '|')

            @staticmethod
            def print_board_nums():
               number_board = [[str(i) for i in range(j+3, (j+1)*3)]for j in range(3)]
               for row in number_board:
                print('|' + '|'.join(row) + '|')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == '']

        def empty_square(self):
            return ' ' in self.board

        def num_empty_squares(self):
            return self.board,count(' ')

       # moves = []
   # for (i, spot) in enumarate(self.board):
        #['x', 'x', '0'] -> [(0, 'x')(1, 'x'), (2, '0')]
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

        letter = 'x' #starting letter
        #iterate while the game still has empty squares
        while game.empty_squares():
            if letter == 'o':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)
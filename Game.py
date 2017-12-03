import Board
import Player

class Game:
    """
    Game of chess containing a board and a history of every play
    """

    def __init__(self):
        self.board = Board.Board()
        self.player1 = Player.Player()
        self.player2 = Player.Player()

    def newGame(self):
        self.board.clear()
        self.player1 = Player.Player()
        self.player2 = Player.Player()

    def load(self,board,player1,player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2


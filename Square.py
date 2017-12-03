import Piece

class Square:
    """
    Single square of a chess board containing :
        - A position (Letter,Number)
        - A chess piece (Piece object)
    """
    def __init__(self,name,color=""):
        self.piece = Piece.Piece(name,color)
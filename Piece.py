class Piece:
    """
    Pawn class :
        range : Maximum number of square a pawn can pass through in a single turn
        name : Pawn label/title ('King' for exemple)
    """
    def __init__(self,name,color = ""):
        self.name = name
        self.color  = color
        self.range = []
        self.capture = []
        self.initRange()

    def __str__(self):
        return self.name

    """
    Initialize each pieces possible moves 
    """
    def initRange(self):
        if self.name == "Tower":
            self.range = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
                          (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)]
            self.capture  = self.range

        elif self.name == "Bishop":
            self.range = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)]
            self.capture = self.range

        elif self.name == "Knight":
            self.range = [(2, 1)]
            self.capture = self.range

        elif self.name == "Queen":
            self.range = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
                          (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                          (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)]
            self.capture = self.range

        elif self.name == "King":
            self.range = [(0,1),(1,0),(1,1)]
            self.capture = self.range

        elif self.name == "Pawn":
            self.range = [(0,1)]
            self.capture = [(1,1)]

    """
    Tells wether or not a piece can perform the specified move
    Returns a boolean and the move itself represented by a movement vector
    """
    def hasRange(self,pos1,pos2):
        lettersOrder = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8}

        if lettersOrder[pos2[0]] < 1 or lettersOrder[pos2[0]] > 8 or pos2[1] < 1 or pos2[1] > 8: #Out of the board
            return False

        """
        Piece move represented by a tuple( +/- x,+/- y) which basically is a x,y vector added to the first pos
        """
        move = (abs(lettersOrder[pos2[0]]-lettersOrder[pos1[0]]),abs(pos2[1]-pos1[1]))

        if move in self.range:
            return True,move

        return False,move
import Square
import Piece

class Board:
    """
    Chess board intialised with 64 empty squares
    """
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    lettersOrder = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8}
    startingPieces = ["Tower","Bishop","Knight","Queen","King","Knight","Bishop","Tower"]

    def __init__(self):
        self.squares = dict()
        self.clear()

    #Display chess board squares positions
    def displayInLine(self):
        for indice, item in self.squares.items():
            print("{} => {}".format(indice, item.piece.name))

    #Display the chess board as a matrix
    def displayMatrix(self):
        print("        ", end=" ")

        #Column Letters
        for k in range(0,8):
            print("{:7}".format(Board.letters[k]), end=" ")
        print()

        #Board Lines
        print("        ", end=" ")
        for l in range(0,8):
            print("{:7}".format("-"), end=" ")
        print()

        for i in range(0,8):
            print("{:7}".format(i+1), end="  ") #Row Numbers
            for j in range(0,8):
                print("{:7}".format(self.squares[(Board.letters[j],i+1)].piece.name), end=" ")
            print()

    #Resets the chess board
    def clear(self):
        for i in range(0, 8) :
            for j in range(8, 0, -1) :
                if j == 8 :
                    self.squares[(Board.letters[i], j)] = Square.Square(Board.startingPieces[i],"black")
                elif j == 1 :
                    self.squares[(Board.letters[i], j)] = Square.Square(Board.startingPieces[i],"white")
                elif j == 7 :
                    self.squares[(Board.letters[i], j)] = Square.Square("Pawn","black")
                elif j == 2 :
                    self.squares[(Board.letters[i], j)] = Square.Square("Pawn","white")
                else :
                    self.squares[(Board.letters[i], j)] = Square.Square("0")

    #Move a piece from a pos to an other, pos : (x,y) -> movement vector
    def movePiece(self,pos1,pos2):
        move = board.squares[pos1].piece.hasRange(pos1, pos2)
        pieceOnTheWay = board.pieceOnTheWay(pos1, pos2)

        print("Piece : {} move : {} from {} to {}".format(board.squares[pos1].piece.name, move, pos1, pos2))
        print("Piece on the way : {}".format(board.pieceOnTheWay(pos1, pos2)))

        if move[0] and not pieceOnTheWay: #Chess piece has the range and falls on an empty square
            if self.squares[pos2].piece.name == "0":
                piecePos2 = self.squares[pos2].piece
                self.squares[pos2].piece = self.squares[pos1].piece
                self.squares[pos1].piece = piecePos2
            else :
                piecePos2 = self.squares[pos2].piece
                color = self.squares[pos1].piece.color
                if piecePos2.name == "King":
                    print("Check")
                else :
                    self.squares[pos2].piece = self.squares[pos1].piece
                    self.squares[pos1].piece = Piece.Piece("0")
                    print("Piece : {} taken by the {} player".format(piecePos2.name,color))

        #else: #Piece stumbling upon on an other piece


    """
    Tells wether the is a piece on the way from pos1 to pos2
    Returns the piece of false if there is none
    """
    def pieceOnTheWay(self,pos1,pos2):
        move = self.squares[pos1].piece.hasRange(pos1, pos2)[1]

        #Allows to either increase or decrease the piece's x and y coordinate depending on the move's direction(up/down)
        if pos1[1] > pos2[1]  : signVertical = -1
        else : signVertical = 1

        if pos1[0] > pos2[0]  : signHorizontal = -1
        else : signHorizontal = 1

        if move[0] == 0: #Vertical move
            for i in range(pos1[1] + signVertical,pos2[1],signVertical):
                if self.squares[(pos1[0],i)].piece.name != "0": return self.squares[(pos1[0],i)].piece

        elif move[1] == 0: #Horizontal move
            for j in range(Board.lettersOrder[pos1[0]] + signHorizontal, Board.lettersOrder[pos2[0]],signHorizontal) :
                letter = Board.letters[j]
                if self.squares[(letter,pos1[1])].piece.name != "0" : return self.squares[(letter,pos1[1])].piece

        elif move[0] == move[1]: #Diagonal move
            for k in range(0 + signHorizontal,move[0],signHorizontal):
                letter = Board.letters[Board.lettersOrder[pos1[0]] + k]
                if self.squares[(letter,pos1[1]+k)].piece.name != "0" : return self.squares[(letter,pos1[1])].piece

        return False

board = Board()
board.displayMatrix()
pos1 = ("A",2)
pos2 = ("A",3)

pos3 = ("A",1)
pos4 = ("A",5)

board.movePiece(pos1,pos2)
board.movePiece(pos3,pos4)

board.displayMatrix()

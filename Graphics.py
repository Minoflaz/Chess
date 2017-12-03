import pyglet
from pyglet.gl import gl
from pyglet.gl.glu import gluLookAt
from pyglet.window import mouse
import numpy as np
import Board

class Graphics(pyglet.window.Window):
    """
    Graphical class to display a chessboard of 8x8 squares
    Its only attributes consist of its width and hight
    """

    # colors
    blackInt4 = (0, 0, 0, 255)
    greenF3 = (0, 1, 0)
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]


    def __init__(self,width,height):
        super().__init__(width, height,resizable=False)

        self.width = width
        self.height = height

        #Used for pieces movements coordinates
        self.coordX = 0
        self.coordY = 0

        self.set_location(400, 32)
        self.set_caption('Chess')
        self.board = Board.Board()

    def on_draw(self):
        self.clear()
        self.drawChessBoard()

    #Draw the chess board
    def drawChessBoard(self):


        #Row/columns Letters and numbers
        self.drawAxises(0.1,0.1,0.8)

        # Draws squares 2 lines  by 2 lines
        self.drawSquares(0.1, 0.1, 0.8)

        #Borders
        self.drawBorders(0.1, 0.0985010999, 0.8) #The minF value is for printing purposes

        # Draws squares 2 lines  by 2 lines
        self.drawPieces(0.1, 0.1, 0.8)


    """
    Draws the chess board borders
    @param squareWidth : float -> each chessboard square width
    @param minF: float -> x and y coordinate where to begin drawing borders (bottom left end corner) 
    @param maxF: float -> x and y coordinate where to stop drawing borders (top right end corner) 
    """
    def drawBorders(self,squareWidth,minF,maxF):
        #Borders
        lines = pyglet.graphics.vertex_list_indexed(4, [0, 1, 0, 2, 3, 1, 3, 2],
                                                    ('v2f', (minF * self.width, minF * self.height,
                                                             (maxF + squareWidth) * self.width, minF * self.height,
                                                             minF * self.width, (maxF + squareWidth) * self.height,
                                                             (maxF + squareWidth) * self.width,
                                                             (maxF + squareWidth) * self.height
                                                             )),
                                                    ('c3B', (20, 10, 120,
                                                             20, 10, 120,
                                                             20, 10, 120,
                                                             20, 10, 120))
                                                    )
        gl.glLineWidth(1.5)
        lines.draw(pyglet.gl.GL_LINES)

    """
    Draws the chess board axises (letters from A to H and numbers from 1 to 8)
    @param squareWidth : float -> each chessboard square width
    @param minF: float -> x and y coordinate where to begin drawing axises (bottom left end corner) 
    @param maxF: float -> x and y coordinate where to stop drawing axises (top right end corner) 
    """
    def drawAxises(self,squareWidth,minF,maxF):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

        #Numbers
        for i in range(7,-1,-1):
            label = pyglet.text.Label(str(i+1), #
                                       font_name='Times New Roman',
                                       font_size=25,
                                       x = (minF  * self.width)/2,
                                       y = (i * (squareWidth*self.height)) +  (((2*minF + squareWidth)*self.height)/2),
                                       anchor_x='center', anchor_y='center')

            label2 = pyglet.text.Label(str(i + 1),
                                      font_name='Times New Roman',
                                      font_size=25,
                                      x=((maxF + 3*squareWidth/2)  * self.width),
                                      y=(i * (squareWidth * self.height)) + (((2 * minF + squareWidth) * self.height)/2),
                                      anchor_x='center', anchor_y='center')
            label.draw()
            label2.draw()

        #Letters
        for i in range(0,8):
            label = pyglet.text.Label(letters[i],
                                       font_name='Times New Roman',
                                       font_size=25,
                                       x = (i * (squareWidth*self.width)) +  (((2*minF + squareWidth)*self.width)/2),
                                       y = ((maxF + 3*squareWidth/2)  * self.height),
                                       anchor_x='center', anchor_y='center')

            label2 = pyglet.text.Label(letters[i],
                                      font_name='Times New Roman',
                                      font_size=25,
                                      x=(i * (squareWidth * self.width)) + (((2 * minF + squareWidth) * self.width)/2),
                                      y=(minF  * self.width)/2,
                                      anchor_x='center', anchor_y='center')
            label.draw()
            label2.draw()


    """
    Draws the chess board squares
    @param squareWidth : float -> each chessboard square width
    @param minF: float -> x and y coordinate where to begin drawing squares (bottom left end corner)
    @param maxF: float -> x and y coordinate where to stop drawing squares (top right end corner)
    """
    def drawSquares(self,squareWidth,minF,maxF):
        for i in np.arange(0.0,maxF,2* squareWidth):
            for j in np.arange(minF,maxF,2 * squareWidth):
                square1 = pyglet.graphics.vertex_list_indexed(4, [0,1,3, 0,2,3],
                                                              ('v2f', ((j + squareWidth) * self.width,(i + minF) * self.height,
                                                                       (j + 2 * squareWidth) * self.width,(i + minF) * self.height,
                                                                       (j + squareWidth) * self.width,(i + squareWidth + minF) * self.height,
                                                                       (j + 2 * squareWidth) * self.width,(i + minF + squareWidth) * self.height
                                                               )),
                                                                ('c3B',(255, 255, 255,
                                                                        255, 255, 255,
                                                                        255, 255, 255,
                                                                        255, 255, 255))
                                                                )
                square2 = pyglet.graphics.vertex_list_indexed(4, [0,1,3, 0,2,3],
                                                                ('v2f', (j * self.width, (i + squareWidth + minF) * self.height,
                                                                        (j + squareWidth) * self.width, (i + squareWidth + minF) * self.height,
                                                                         j * self.width, (i + 2 * squareWidth + minF) * self.height,
                                                                        (j + squareWidth) * self.width, (i + 2 * squareWidth + minF) * self.height
                                                                )),
                                                              ('c3B', (255, 255, 255,
                                                                       255, 255, 255,
                                                                       255, 255, 255,
                                                                       255, 255, 255))
                                                              )
                square3 = pyglet.graphics.vertex_list_indexed(4, [0, 1, 3, 0, 2, 3],
                                                              ('v2f', (j * self.width, (i + minF) * self.height,
                                                                       (j + squareWidth) * self.width,
                                                                       (i + minF) * self.height,
                                                                       j * self.width,
                                                                       (i + squareWidth + minF) * self.height,
                                                                       (j + squareWidth) * self.width,
                                                                       (i + squareWidth + minF) * self.height
                                                                       )),
                                                              ('c3B', (105,105,105,
                                                                       105, 105, 105,
                                                                       105, 105, 105,
                                                                       105, 105, 105))
                                                              )
                square4 = pyglet.graphics.vertex_list_indexed(4, [0, 1, 3, 0, 2, 3],
                                                              ('v2f', ((j + squareWidth) * self.width,
                                                                       (i + minF + squareWidth) * self.height,
                                                                       (j + 2 * squareWidth) * self.width,
                                                                       (i + minF + squareWidth) * self.height,
                                                                       (j + squareWidth) * self.width,
                                                                       (i + 2 * squareWidth + minF) * self.height,
                                                                       (j + 2 * squareWidth) * self.width,
                                                                       (i + 2 * squareWidth + minF) * self.height
                                                                       )),
                                                              ('c3B', (105,105,105,
                                                                       105, 105, 105,
                                                                       105, 105, 105,
                                                                       105, 105, 105))
                                                              )
                square1.draw(pyglet.gl.GL_TRIANGLES)
                square2.draw(pyglet.gl.GL_TRIANGLES)
                square3.draw(pyglet.gl.GL_TRIANGLES)
                square4.draw(pyglet.gl.GL_TRIANGLES)

    def drawPieces(self,squareWidth,minF,maxF):
        blackPieces = ['\u265C','\u265E','\u265D','\u265B','\u265A']
        whitePieces = ['\u2656','\u2658','\u2657','\u2655','\u2654']
        piece = 0

        #Pawn drawing
        for i in np.arange(0,maxF,squareWidth) :
            blackPawn = pyglet.text.Label(
                u'\u265F',
                font_size=56,
                color=(0,0,0,255),
                x=(minF + squareWidth / 2 + i) * self.width, y=(maxF - squareWidth / 2) * self.height,
                anchor_x='center', anchor_y='center')
            blackPawn.draw()

            whitePawn = pyglet.text.Label(
                u'\u2659',
                font_size=56,
                color=(0,0,0, 255),
                x=(minF + squareWidth / 2 + i) * self.width, y=(2 * minF + squareWidth / 2) * self.height,
                anchor_x='center', anchor_y='center')

            whitePawn.draw()

        #All other pieces
        for i in np.arange(0,maxF/2+squareWidth,squareWidth):
            blackPiece = pyglet.text.Label(
                u'' + blackPieces[piece],
                font_size=56,
                color=(0, 0, 0, 255),
                x=(minF + squareWidth / 2 + i) * self.width, y=(maxF + squareWidth / 2) * self.height,
                anchor_x='center', anchor_y='center')
            blackPiece.draw()

            whitePiece = pyglet.text.Label(
                u'' + whitePieces[piece],
                font_size=56,
                color=(0, 0, 0, 255),
                x=(minF + squareWidth / 2 + i) * self.width, y=(minF + squareWidth / 2) * self.height,
                anchor_x='center', anchor_y='center')
            whitePiece.draw()

            #Queen and king
            if piece <3:
                blackPiece = pyglet.text.Label(
                    u'' + blackPieces[piece],
                    font_size=56,
                    color=(0, 0, 0, 255),
                    x=(maxF + squareWidth / 2 - i) * self.width, y=(maxF + squareWidth / 2) * self.height,
                    anchor_x='center', anchor_y='center')
                blackPiece.draw()

                whitePiece = pyglet.text.Label(
                    u'' + whitePieces[piece],
                    font_size=56,
                    color=(0, 0, 0, 255),
                    x=(maxF + squareWidth / 2 - i) * self.width, y=(minF + squareWidth / 2) * self.height,
                    anchor_x='center', anchor_y='center')
                whitePiece.draw()
            piece += 1

    def on_mouse_press(self,x, y, button, modifiers):
        coordX = int(x/100)
        coordY = int(y/100)
        if 0 < coordX < 9 and 0 < coordY < 9:
            self.coordX = coordX
            self.coordY = coordY
            print("Mouse press on {},{}".format(Graphics.letters[coordX-1],coordY))

    def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        blackPawn = pyglet.text.Label(
            u'\u265F',
            font_size=56,
            color=(0, 0, 0, 255),
            x=x, y=y,
            anchor_x='center', anchor_y='center')
        blackPawn.draw()

    def on_mouse_release(self,x, y, button, modifiers):
        coordX = int(x / 100)
        coordY = int(y / 100)
        #if movement inbounds and no null movement
        if 0 < coordX < 9 and 0 < coordY < 9 and (self.coordX != coordX or self.coordY != coordY):
            print("Mouse move from {},{} to {},{}".format(Graphics.letters[self.coordX - 1], self.coordY,Graphics.letters[coordX - 1], coordY))

    def setupGl(self):
        gl.glViewport(0, 0, self.width, self.height)

        # sets the projection
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(-2, 2, -2, 2, -2, 2)

        # sets the model view
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        gluLookAt(0,0,1, #eye
                  0,0,0, #lookAt
                  0,1,0) #up axis

    def drawChessBoardGl(self):
        self.setupGl()

        # clears the background with the background color
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        # square color
        gl.glColor3f(*self.greenF3)

        squareWidth = 0.4
        minF = -1.6
        maxF = 1.6

        for h in np.arange(0.0,2 * maxF,2 * squareWidth):
            #Draws the chess board 2 lines by 2 lines
            for i in np.arange(minF,maxF,2 * squareWidth):
                # draws a square
                gl.glBegin(gl.GL_QUADS)
                gl.glVertex3f(i+squareWidth, minF+squareWidth+h, 0)
                gl.glVertex3f(i, minF + squareWidth+h, 0)
                gl.glVertex3f(i, minF+h, 0)
                gl.glVertex3f(i+squareWidth, minF+h, 0)
                gl.glEnd()

                gl.glBegin(gl.GL_QUADS)
                gl.glVertex3f(i + 2 * squareWidth, minF + 2 * squareWidth+h, 0)
                gl.glVertex3f(i + squareWidth, minF + 2 * squareWidth+h, 0)
                gl.glVertex3f(i + squareWidth, minF + squareWidth+h, 0)
                gl.glVertex3f(i + 2 * squareWidth, minF + squareWidth+h, 0)
                gl.glEnd()

        pyglet.graphics.draw(8, pyglet.gl.GL_LINES,
                             ("v2f", (minF, minF,minF , maxF,maxF,minF,maxF,maxF,minF,minF,maxF,minF,minF,maxF,maxF,maxF)),
                             ('c3B', (0, 255, 0, 0, 255, 0,0, 255, 0,0, 255, 0,0, 255, 0,0, 255, 0,0, 255, 0,0, 255, 0))
                             )

graphics = Graphics(1000,1000)
pyglet.app.run()
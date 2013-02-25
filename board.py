import pygame
from screen import Tile

#The size of each block in pixels (they're squares so only need one measurement)
BLOCKSIZE = 32 
#The height and width of the board in a measurement of blocks  
BOARDWIDTH = 20
BOARDHEIGHT = 20

# Pixel coordinates for square creation
STARTX = 0
STARTY = 0
ENDX = (BOARDWIDTH * BLOCKSIZE) + STARTX
ENDY = (BOARDHEIGHT * BLOCKSIZE) + STARTY

BLANKCOLOR = (137, 155, 141) # White


class BoardSquare (Tile):
  """
  This class represents the squares on the game board.
  It inherits the Tile class from screen.
  Attrs. xcoord and ycoord refer to the squares x and y coordinates
  on the board i.e. square (0,0); square (1,0); square (2,0); etc
  Attr player refers to what player the square is associated with.
  If player is 0, then the square is blank. 
  """
  
  def __init__(self, x, y, size, color, xcoord, ycoord):
    Tile.__init__(self, x, y, size, color)
    self.xcoord = xcoord
    self.ycoord = ycoord
    player = 0
    
  def setPlayer(player):
    self.player = player



class Board:
  """
  This class represents the playing board.
  It contains a 2D list of BoardSquare objects.
  They are indexed so that 0,0 is in the top left corner
  """

  def __init__(self):
    ### Creating the squares ###
    self.squares = []
    xtemp = 0 # Used for giving the tiles xcoord
    ytemp = 0 # Used for giving the tiles ycoord
    for x in xrange(STARTX, ENDX, BLOCKSIZE):
      new = []
      ytemp = 0
      for y in xrange(STARTY, ENDY, BLOCKSIZE):
        newSquare = BoardSquare(x, y, BLOCKSIZE, BLANKCOLOR, xtemp, ytemp)
        new.append(newSquare)
        ytemp += 1 # Go on to the next column
      self.squares.append(new)
      xtemp += 1 # Go on to the next row
      
      
  def draw(self, screen):
    for squaresList in self.squares:
      for square in squaresList:
        square.draw(screen)
      
      
      
      
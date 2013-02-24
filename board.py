import pygame
import screen

#The size of each block in pixels (they're squares so only need measurement)
BLOCKSIZE = 16 
#The height and width of the board in a measurement of blocks  
BOARDWIDTH = 20
BOARDHEIGHT = 20


class BoardSquare (Tile):
  """
  This class represents the squares on the game board.
  It inherits the Tile class from screen.
  Attrs. xcoord and ycoord refer to the squares x and y coordinates
  on the board i.e. square (0,0); square (1,0); square (2,0); etc
  Attr player refers to what player the square is associated with.
  If player is 0, then the square is blank. 
  """
  
  def __init__(self, xcoord, ycoord)
    self.xcoord = xcoord
    self.ycoord = ycoord
    player = 0
    
  def setPlayer(player)
    self.player = player



class Board

  def __init__(self)
  tiles = []
    for x in xrange(0, self.width, BLOCKSIZE):
      new = []
      for y in xrange(0, self.height, BLOCKSIZE):
        newTile = Tile(x, y, BLOCKSIZE, (255, 255, 255))
        new.append(newTile)
      self.tiles.append(new)
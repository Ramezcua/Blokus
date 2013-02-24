import pygame

class Tile:
  """ 
  This is the tile class for tiles on the screen.
  x and y denote the top left corner of the tile in pixels
  where xpx is the horizontal and ypx is the vertical.
  Tiles are squares so only one measurement is needed
  to create them.
  Color is given in an rgb tuple (r,g,b).
  """
      
  def __init__(self, x, y, size, color):
    self.x = x
    self.y = y
    self.size = size
    self.color = color
    
  def draw(self, screen):
    """ 
    This function takes a screen as an arg (from pygame)
    It will the draw the tile on the screen using its attributes
    """
    
    pygame.draw.rect(screen, self.color, ((self.x, self.y), (self.size, self.size)), 0)
    
  def setColor(self, color):
    self.color = color
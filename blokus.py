import pygame

# Screen measurements
S_WIDTH = 800
S_HEIGHT = 800
S_CENTERX = S_WIDTH/2
S_CENTERY = S_HEIGHT/2
BACKGROUND_COL = (255, 255, 255)

RUNNING = True

class Board:
  def __init__(self, screen, screen_width, screen_height):
    """ Board Class that will hold all of the pieces """
    self.screen = screen
    self.screen_width = screen_width
    self.screen_height = screen_height    
    
    # The size of one side of a block (in px).  This is a square
    self.blockSize = 20 
    
	# Board measurements
    self.bBlockWidth = 20
    self.bBlockHeight = 20
    # Converting board height and width to px
    self.bPxWidth = self.bBlockWidth * self.blockSize
    self.bPxHeight = self.bBlockHeight * self.blockSize
    # Getting the coordinates for the top left corner of the board on the screen
    # Need this to draw the board
    self.bLeft = S_CENTERY - self.bPxWidth/2
    self.bTop = S_CENTERX - self.bPxHeight/2 
    self.color = (0, 0, 0) # Line Color = Black

  def draw(self):
    pygame.draw.rect(self.screen, self.color, ((self.bLeft, self.bTop), (self.bPxWidth, self.bPxWidth)), 1)

# Initialization of important game objects
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
clock = pygame.time.Clock()
board = Board(screen, S_WIDTH, S_HEIGHT)

while RUNNING:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      RUNNING = False
 
  # Color background     
  screen.fill(BACKGROUND_COL)
  
  board.draw()
    
  pygame.display.flip() # This draws everything on the screen
  clock.tick(240) 



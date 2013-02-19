import pygame

S_WIDTH = 800
S_HEIGHT = 800
S_CENTERX = S_WIDTH/2
S_CENTERY = S_HEIGHT/2

BACKGROUND_COL = (255, 255, 255)

RUNNING = True

class Board:
  def __init__(self, screen, screen_width, screen_height):
    self.screen = screen
    self.screen_width = screen_width
    self.screen_height = screen_height    
    
    # The size of one side of a block (in px).  This is a square
    self.blockSize = 20 
    
	# Board measurements
    self.bBlockWidth = 20
    self.bBlockHeight = 20
    self.bPxWidth = self.bBlockWidth * self.blockSize
    self.bPxHeight = self.bBlockHeight * self.blockSize
    self.bLeft = S_CENTERY - self.bPxWidth/2
    self.bTop = S_CENTERX - self.bPxHeight/2 
    self.color = (0, 0, 0) # Line Color = Black

  def draw(self):
    pygame.draw.rect(self.screen, self.color, ((self.bLeft, self.bTop), (self.bPxWidth, self.bPxWidth)), 1)

  
    



screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
clock = pygame.time.Clock()
board = Board(screen, S_WIDTH, S_HEIGHT)

while RUNNING:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      RUNNING = False
      
  screen.fill(BACKGROUND_COL)
  
  board.draw()
    
  pygame.display.flip()
  clock.tick(240)



import pygame
from board import *
from screen import *

pygame.display.set_caption("Blokus")

S_WIDTH = 640
S_HEIGHT = 640
BACKGROUND_COL = (219, 225, 221) #Black

# Initialization of important game objects
RUNNING = True
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
clock = pygame.time.Clock()

# Initializing board
board = Board()

while RUNNING:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      RUNNING = False
 
  # Color background     
  screen.fill(BACKGROUND_COL)
  
  board.draw(screen)
    
  pygame.display.flip() # This draws everything on the screen
  clock.tick(100) 



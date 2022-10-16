###############################
# Title: PONG Game
# Author: Ethan Pereira
###############################

import pygame
from sympy import false
from paddle import Paddle
from ball import Ball

# Initializing the constructor
pygame.init()

# Set some global variables 
WIDTH, HEIGHT = 700, 500
WHITE = (255, 255, 254)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Get the system default Font - Font styles are different for Operating systems. 
# Example: Mac does not have the Font Arial
# Set the Font Size to 35
font = pygame.font.Font(pygame.font.get_default_font(), 35)

# Setting the FONT Style for the score to COMICSANS style
# Set the Font size to 50
SCORE_FONT = pygame.font.SysFont("comicsans", 50)

RULES_FONT_LARGE = pygame.font.Font(pygame.font.get_default_font(), 30)
RULES_FONT_SMALL = pygame.font.Font(pygame.font.get_default_font(), 15)

# Store the screen size
size = (WIDTH, HEIGHT)

gameDisplay = pygame.display

# Set caption of window screen
gameDisplay.set_caption('PONG by Ethan')

# Setting the size of the window  

surface = gameDisplay.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def gameOverScreen():
  
  # Write text to the screen
  text = font.render("GAME OVER", 1, WHITE)
  surface.blit(text, (WIDTH//2 - text.get_width() //
                            2, HEIGHT//2 - text.get_height()//2))
  

def startScreen():
  # Two different ways to get a message to the screen:
  # Draw an image file to the screen
  # Load the background image for the start screen
  background = pygame.image.load("Images/Titlescreen.png")
  surface.blit(background, (WIDTH, HEIGHT))

  # Write text to the screen
  text = font.render("Press x to start the game", 1, WHITE)

  surface.blit(text, (150, HEIGHT/3))

  surface.blit(RULES_FONT_SMALL.render("First player to score 10 WINS.",1,WHITE), (250, 300))
  surface.blit(RULES_FONT_SMALL.render("To exit anytime, press X.",1,WHITE), (270, 350))

  # Write the image and the text to the screen, in that order
  pygame.display.flip()
  startGame = False

  # Loop that waits for the user to quit the game, or press x to start the game
  while (not startGame):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:  # Pressing the x Key will quit the game
          startGame = True

def main():  # main method to run the game
  # define the left paddle, 20 pixels wide, 20 pixels from the left side
  leftPaddle = Paddle(WHITE, 20, 100)
  leftPaddle.rect.x = 10
  leftPaddle.rect.y = 200

  # define the right paddle, 10 pixels wide, 20 pixels from the right side
  rightPaddle = Paddle(WHITE, 20, 100)
  rightPaddle.rect.x = 670
  rightPaddle.rect.y = 200

  # define the ball 10 pixels by 10 pixels starts in the middle of the screen
  ball = Ball(WHITE, 10, 10)
  ball.rect.x = 315
  ball.rect.y = 195

  # This will be a list that will contain all the sprites we intend to use 
  # in our game.
  all_sprites_list = pygame.sprite.Group()

  # Add the paddles and ball to the list of sprites
  all_sprites_list.add(leftPaddle)
  all_sprites_list.add(rightPaddle)
  all_sprites_list.add(ball)
  
  game = True
  clock = pygame.time.Clock()
  
  #This counts the score of the game 
  player1Score = 0
  player2Score = 0

  while game:  # Game loop, takes user input, keeps score
    surface.fill(BLACK)

    text = SCORE_FONT.render(str(player1Score), 1, WHITE)
    surface.blit(text, (250, 19))
    text = SCORE_FONT.render(str(player2Score), 1, WHITE)
    surface.blit(text, (380, 19))
  
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:  # Pressing the x Key will quit the game
          game = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and leftPaddle.rect.y > 0:
      leftPaddle.moveUp(5)
    if keys[pygame.K_s] and leftPaddle.rect.y < (HEIGHT - 100) :
      leftPaddle.moveDown(5)
    if keys[pygame.K_UP]and rightPaddle.rect.y > 0:
      rightPaddle.moveUp(5)
    if keys[pygame.K_DOWN]and rightPaddle.rect.y < (HEIGHT - 100) :
      rightPaddle.moveDown(5)

    # Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, leftPaddle) or pygame.sprite.collide_mask(ball, rightPaddle):
      ball.bounce()
    # --- Game logic should go here
    all_sprites_list.update()
        
    if ball.rect.y > HEIGHT or ball.rect.y < 0:
      ball.velocity[1] = -ball.velocity[1]

    #Check if ball goes off the left side of the screen 
    if ball.rect.x < 0:
      player2Score += 1
      ball.reset()
    #Check if the ball goes off the right side of the screen 
    elif ball.rect.x > WIDTH:
      player1Score += 1
      ball.reset()

    if player1Score ==10:
      gameOverScreen()
      pygame.time.delay(5000)
      game = False
    elif player2Score ==10:
      gameOverScreen()
      pygame.time.delay(5000)
      game = False 

      
    # --- Drawing code should go here
    # First, clear the screen to black.
    # Draw the net
    pygame.draw.line(surface, WHITE, [319, 0], [319, 500], 5)
    
    # Now let's draw all the sprites in one go. (For now we only have 
    # 2 sprites!)
    all_sprites_list.draw(surface)

    # Display scores:

    # Update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)


startScreen()
main()

pygame.quit()

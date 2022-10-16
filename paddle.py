import pygame


WHITE = (255, 255, 255)


class Paddle(pygame.sprite.Sprite):

    # This class represents a paddle. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the paddle, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    # Move the paddle up the screen
    def moveUp(self, pixels):
        self.rect.y -= pixels

    # Move the paddle down the screen
    def moveDown(self, pixels):
        self.rect.y += pixels


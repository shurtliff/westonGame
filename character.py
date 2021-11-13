import pygame


class Character:
    """Represents a chess piece."""

    def __init__(self, spriteSheet, screen, tiles):
        """Initialize attributes to represent a ches piece."""
        self.height = 32
        self.width = 32
        self.spriteSheet = spriteSheet
        self.screen = screen
        self.tiles = tiles
        self.name = ''
        self.color = ''

        # Start each piece off at the top left corner.
        self.x, self.y = 0.0, 0.0
        self.image = spriteSheet.get_image(self.x, self.y, self.height, self.width)

    def blitme(self):
        """Draw the piece at its current location."""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)
    def move(self, move):
        x = self.x+move[0]
        y = self.y+move[1]
        w = self.width
        h = self.height
        playerrec = pygame.Rect([x,y,w,h])
        check = False
        if (playerrec.collidelistall(self.tiles)): #this tests every tile with the player rectangle
            return
        self.x = x
        self.y = y

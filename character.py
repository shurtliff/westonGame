import pygame
from constants import *


class Character:
    """Represents a chess piece."""

    def __init__(self, spriteSheet, screen, tiles, mapObject):
        """Initialize attributes to represent a ches piece."""
        self.height = 32
        self.width = 32
        self.spriteSheet = spriteSheet
        self.screen = screen
        self.tiles = tiles
        self.name = ''
        self.color = ''
        self.mapObject = mapObject
        self.collection = 0

        # Start each piece off at the top left corner.
        self.x, self.y = mapObject.x, mapObject.y
        self.image = spriteSheet.get_image(0, 0, self.height, self.width)

    def blitme(self):
        """Draw the piece at its current location."""
        # self.rect = self.mapObject.get_rect()
        # self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, [(SCREENWIDTH/2), (SCREENHEIGHT/2)])
    def move(self, move):
        x = self.mapObject.x+move[0]
        y = self.mapObject.y+move[1]
        w = self.mapObject.width
        h = self.mapObject.height
        playerrec = pygame.Rect([x,y,w,h])
        check = False
        if (playerrec.collidelistall(self.tiles)): #this tests every tile with the player rectangle
            return
        self.mapObject.x = x
        self.mapObject.y = y
    def collectItem(self, collectables):
        rect = self.getRect()
        removCol = []
        for colItem in collectables:
            if colItem.boundingBox.colliderect(rect):
                colItem.hide()
                self.collection += 1
    def getRect(self):
        x = self.mapObject.x
        y = self.mapObject.y
        w = self.mapObject.width
        h = self.mapObject.height
        return pygame.Rect([x,y,w,h])

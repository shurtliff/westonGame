class Collectable :
    def __init__(self, tile, x, y, boundingBox):
        self.boundingBox = boundingBox
        self.tile = tile
        self.show = 1
        self.x = x
        self.y = y

    def isVisible(self):
        return self.show

    def hide(self):
        self.show = 0

    # def blit(self, screen, camera, tileWidth, tileHeight, screenWith, screenHeight):
    #     if self.show == 1 :
    #         screen.blit(self.surface, [(self.boundingBox.x*tileWidth) - camera.x +(screenWith/2), (self.boundingBox.y*tileHeight) - camera.y + (screenHeight/2)])


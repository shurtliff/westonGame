import os
import level1
import level2
import level

#initialize pygame & window
from character import Character
from collectable import Collectable
from constants import *
from spritesheet import SpriteSheet

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

#caption for the game
pygame.display.set_caption("My first game in pygame")
#game loop

level = level.Level()
level.GO('maps/map.tmx')
level.GO('maps/map2.tmx')
level.GO('maps/map3.tmx')

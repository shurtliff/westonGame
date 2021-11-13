import pygame
import sys
import os
import pytmx
from pytmx.util_pygame import load_pygame

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
import level2

level_1 = level2.Level2()
level_1.GO()

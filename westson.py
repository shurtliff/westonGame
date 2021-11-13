import pygame
import sys
import os
import pytmx
from pytmx.util_pygame import load_pygame

#initialize pygame & window
from character import Character
from constants import *
from spritesheet import SpriteSheet

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

#caption for the game
pygame.display.set_caption("My first game in pygame")
tiled_map = load_pygame('maps/map.tmx')
tilewidth = tiled_map.tilewidth
tileheight = tiled_map.tileheight
collectables = tiled_map.get_layer_by_name('collectables')
collision = tiled_map.get_layer_by_name('collision')
tiles = []
for x, y, tile in collision.tiles():
        if (tile):
             tiles.append(pygame.Rect([(x*tilewidth), (y*tileheight), tilewidth, tileheight]));
filename = 'sprites/characters.png'
characters = SpriteSheet(filename)

        # Create a black king.
# my_player = (68, 70, 85, 85)
# my_player_image = characters.image_at(my_player)

CAMERA = tiled_map.get_object_by_name("player")
player = Character(characters, SCREEN, tiles, CAMERA)
player.name = 'bugSplat'
#game loop
while True:
    for events in pygame.event.get(): #get all pygame events
        if events.type == pygame.QUIT: #if event is quit then shutdown window and program
            pygame.quit()
            sys.exit()
        for layer in tiled_map.layers:
            if isinstance(layer, pytmx.TiledTileLayer) and (layer!=collision):
                for x, y, tile in layer.tiles():
                    if (tile):
                        SCREEN.blit(tile, [(x*tilewidth) - CAMERA.x +(SCREENWIDTH/2) , (y*tileheight) - CAMERA.y + (SCREENHEIGHT/2)])

            # elif isinstance(layer, pytmx.TiledObjectGroup):
            #     for object in layer:
            #         if (object.type=='Player'):
            #             SCREEN.blit(player.image, [object.x - CAMERA.x +(SCREENWIDTH/2), object.y - CAMERA.y + (SCREENHEIGHT/2)])
        pos = [0,0]
        for events in pygame.event.get(): #get all pygame events
                if events.type == pygame.QUIT: #if event is quit then shutdown window and program
                    pygame.quit()
                    sys.exit()

        PRESSED = pygame.key.get_pressed()

        if PRESSED[pygame.K_LEFT]:
                pos[0]-=10
        elif PRESSED[pygame.K_RIGHT]:
                pos[0]+=10
        if PRESSED[pygame.K_UP]:
                pos[1]-=10
        elif PRESSED[pygame.K_DOWN]:
                pos[1]+=10
        # tiled_map.get_object_by_name("player").x += pos[0]
        # tiled_map.get_object_by_name("player").y += pos[1]
        player.move((pos[0], pos[1]))

        player.blitme()
        pygame.display.update()

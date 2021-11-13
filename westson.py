import pygame
import sys
import os
import pytmx
from pytmx.util_pygame import load_pygame

#initialize pygame & window
from character import Character
from spritesheet import SpriteSheet

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
SCREENWIDTH = 500
SCREENHEIGHT = 500
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)

#caption for the game
pygame.display.set_caption("My first game in pygame")
tiled_map = load_pygame('maps/testing.tmx')
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

player = Character(characters, SCREEN, tiles)
player.name = 'bugSplat'
CAMERA = tiled_map.get_object_by_name("player")
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
                        SCREEN.blit(tile, [x*tilewidth,y*tileheight])

            # elif isinstance(layer, pytmx.TiledObjectGroup):
            #     for object in layer:
            #         if (object.type=='player'):
            #             SCREEN.blit(player, (object.x, object.y))
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

        player.move((pos[0], pos[1]))

        player.blitme()
        pygame.display.update()

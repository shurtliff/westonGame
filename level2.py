import sys
import pytmx
from pytmx.util_pygame import load_pygame

#initialize pygame & window
from character import Character
from collectable import Collectable
from constants import *
from spritesheet import SpriteSheet
class Level2 :
    def GO(self):
        tiled_map = load_pygame('maps/map2.tmx')
        TILEWIDTH = tiled_map.tilewidth
        TILEHEIGHT = tiled_map.tileheight
        collectables = tiled_map.get_layer_by_name('collectables')
        endLayer = tiled_map.get_layer_by_name('endlayer')
        COLLISION = tiled_map.get_layer_by_name('collision')
        tiles = []
        for x, y, tile in COLLISION.tiles():
            if (tile):
                 tiles.append(pygame.Rect([(x*(TILEWIDTH)), (y*TILEHEIGHT), TILEWIDTH, TILEHEIGHT]));
        collects = []
        for x, y, colTile in collectables.tiles():
            if (colTile):
                collects.append(Collectable(colTile, x, y, pygame.Rect([(x*TILEWIDTH), (y*TILEHEIGHT), TILEWIDTH, TILEHEIGHT])))
        ends = []
        for x, y, endTile in endLayer.tiles():
            if (endTile):
                 ends.append(pygame.Rect([(x*(TILEWIDTH)), (y*TILEHEIGHT), TILEWIDTH, TILEHEIGHT]));
        filename = 'sprites/characters.png'
        characters = SpriteSheet(filename)
        pygame.key.set_repeat(1, 50)
                # Create a black king.
        # my_player = (68, 70, 85, 85)
        # my_player_image = characters.image_at(my_player)

        CAMERA = tiled_map.get_object_by_name("player")
        player = Character(characters, SCREEN, tiles, CAMERA)
        player.height = TILEWIDTH
        player.width = TILEWIDTH
        player.name = 'bugSplat'
        won = False
        #game loop
        while won == False:
            for events in pygame.event.get(): #get all pygame events
                if events.type == pygame.QUIT: #if event is quit then shutdown window and program
                    pygame.quit()
                    sys.exit()
                for layer in tiled_map.layers:
                    if isinstance(layer, pytmx.TiledTileLayer) and (layer!=COLLISION) and ((layer != collectables) ):
                        for x, y, tile in layer.tiles():
                            if (tile):
                                SCREEN.blit(tile, [(x*TILEWIDTH) - CAMERA.x +(SCREENWIDTH/2) , (y*TILEHEIGHT) - CAMERA.y + (SCREENHEIGHT/2)])

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
                player.collectItem(collects)
                player.blitme()
                if player.collection > collectables.collect_count :
                    won = player.checkLevel(ends)
                for collect in collects :
                    if collect.show :
                        SCREEN.blit(collect.tile, [(collect.x*TILEWIDTH) - CAMERA.x +(SCREENWIDTH/2) , (collect.y*TILEHEIGHT) - CAMERA.y + (SCREENHEIGHT/2)])
                pygame.display.update()



#Main
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import os

import core
import player
import dungeon_room as dr

#Constants
FRAME_RATE = 60

'''
FUNCTIONS
'''

#Load Sprites Function
def load_sprite(sprite_path):
    sprite = []
    exists = True
    tile_num = 0
    
    while exists:
        if os.path.isfile(os.path.join('images', sprite_path, 'tile' + convert_to_three_digits(tile_num) + '.png')):
            sprite.append(pygame.image.load(os.path.join('images', sprite_path, 'tile' + convert_to_three_digits(tile_num) + '.png')))
            tile_num += 1
        else:
            exists = False
    
    return sprite


#Convert to Three Digits Helper Function
def convert_to_three_digits(num):
    if num < 10:
        return '00' + str(num)
    elif num < 100:
        return '0' + str(num)
    else:
        return str(num)


#Load All Sprites Function
def load_all_sprites():
    sprites = {}

    with os.scandir("images") as it:
        for entry in it:
            sprites[entry.name] = load_sprite(entry.name)

    return sprites

#Strip Tiles from Sheet Function
def strip_from_sheet(sheet, start, size, columns, rows):
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)

            frames.append(sheet.subsurface(pygame.Rect(location, size)))
    return frames


#Draw All Sprites
def draw_sprites(screen, object_list, sprite_list):
    for obj in object_list:
        if obj.visible and obj.sprite_index != None:

            img = sprite_list[obj.sprite_index][obj.image_index]
            img.set_alpha(int(obj.image_alpha * 255))
            screen.blit(img,(obj.x, obj.y))
            
            if obj.image_speed == 1:
                obj.image_index += 1
                
                if obj.image_index >= obj.sprite_frames:
                    obj.image_index = 0

#Display Room Tiles
def display_room(screen, room, tiles, tile_size):
    for r in range(room.room_height):
        for c in range(room.room_width):
            screen.blit(tiles[room.tiles[r][c]],(c * tile_size, r * tile_size))


def engine_main():
    
    #Initialize PyGame
    pygame.mixer.pre_init()
    pygame.mixer.init()
    pygame.init()
    
    #Set the Icon
    logo = pygame.image.load("images/logo.png")
    pygame.display.set_icon(logo)
    
    #Set the Window Title
    pygame.display.set_caption('CS230 Project')
    
    #Create a Surface on the Screen
    screen = pygame.display.set_mode((640, 360))
    
    #Create a Background Fill
    screen.fill(pygame.Color('#ffefff'))
    
    #Define a variable for the main loop
    running = True
    
    #Set the PyGame Clock
    clock = pygame.time.Clock()
    
    #Load all Sprites
    sprites = load_all_sprites()
    
    #Load Tilesets
    basic_tilemap_image = pygame.image.load(os.path.join('tilesets', 'til_basic_tiles.png'))
    basic_tiles = strip_from_sheet(basic_tilemap_image, (0, 0), (core.TILE_SIZE, core.TILE_SIZE), 2, 2)
    
    #Create an Input Manager
    input_manager = core.InputManager()
    
    #Create an Objects List
    objects = []
    
    #Create a Test Room
    test_room = dr.DungeonRoom(40, 23)
    
    #Create the Player
    main_player = core.instance_create(32, 32, player.Player())
    objects.append(main_player)
    
    #Assign a Room Layout
    for r in range(23):
        for c in range(40):
            if (r == 0 or c == 0 or r == 22 or c == 39):
                test_room.set_tile(c, r, 1, 1)
    
    #Assign the Current Room
    current_room = test_room
    
    #Main Loop
    while running:
        #Update Frame Rate
        time_delta = clock.tick(FRAME_RATE)/1000.0      


        #Event Handling
        for event in pygame.event.get():
            
            #Event: QUIT
            if event.type == pygame.QUIT:
                #Set Running to False
                running = False
            
            #Event: INPUT
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if input_manager.left != 1:
                        input_manager.left_pressed = 1
                    
                    input_manager.left = 1
                else:
                    input_manager.left = 0
                    input_manager.left_pressed = 0

                if event.key==pygame.K_RIGHT:
                    if input_manager.right != 1:
                        input_manager.right_pressed = 1
                    
                    input_manager.right = 1
                else:
                    input_manager.right = 0
                    input_manager.right_pressed = 0

                if event.key==pygame.K_UP:
                    if input_manager.up != 1:
                        input_manager.up_pressed = 1
                    
                    input_manager.up = 1
                else:
                    input_manager.up = 0
                    input_manager.up_pressed = 0

                if event.key==pygame.K_DOWN:
                    if input_manager.down != 1:
                        input_manager.down_pressed = 1
                    
                    input_manager.down = 1
                else:
                    input_manager.down = 0
                    input_manager.down_pressed = 0
                    
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    input_manager.left_pressed = 0
                    input_manager.left = 0
                    
                if event.key==pygame.K_RIGHT:
                    input_manager.right_pressed = 0
                    input_manager.right = 0
                    
                if event.key==pygame.K_UP:
                    input_manager.up_pressed = 0
                    input_manager.up = 0
                    
                if event.key==pygame.K_DOWN:
                    input_manager.down_pressed = 0
                    input_manager.down = 0

                

        #Run Update Logic
        for i in range(len(objects)):
            objects[i].update(current_room, input_manager)
        
        #Clear the Old Screen
        screen.fill(pygame.Color('#ffefff'))

        #Draw Graphics
        display_room(screen, current_room, basic_tiles, core.TILE_SIZE)
        
        draw_sprites(screen, objects, sprites)
        
        #Update the Display
        pygame.display.update()
      
        
#Run main
engine_main()
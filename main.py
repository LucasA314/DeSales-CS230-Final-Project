

#Main
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import os

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
    screen = pygame.display.set_mode((360, 640))
    
    #Create a Background Fill
    screen.fill(pygame.Color('#ffefff'))
    
    #Define a variable for the main loop
    running = True
    
    #Set the PyGame Clock
    clock = pygame.time.Clock()
    
    #Main Loop
    while running:
        #Update Frame Rate
        time_delta = clock.tick(FRAME_RATE)/1000.0

        #Load all Sprites
        sprites = load_all_sprites()
        

        #Event Handling
        for event in pygame.event.get():
            
            #Event: QUIT
            if event.type == pygame.QUIT:
                #Set Running to False
                running = False
            
            #Event: INPUT


        #Run Update Logic

        
        #Clear the Old Screen
        screen.fill(pygame.Color('#ffefff'))

        #Draw Graphics
        
        
        #Update the Display
        pygame.display.update()
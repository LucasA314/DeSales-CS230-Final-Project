

#Main
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import os

import core
import music_core
import events_core as ec
from constants import *
import player
import enemy
import textbox_objects
import title_menu
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

#MainManager Class: Omnipotent Class that Gives Life to All Else        
class MainManager():
    def __init__(self):
        self.quit = False

        #Load all Sprites
        self.sprites = load_all_sprites()
        
        #Load Tilesets
        self.basic_tilemap_image = pygame.image.load(os.path.join('tilesets', 'til_basic_tiles.png'))
        self.basic_tiles = strip_from_sheet(self.basic_tilemap_image, (0, 0), (core.TILE_SIZE, core.TILE_SIZE), 2, 3)
        
        #Create an Input Manager
        self.im = core.InputManager()
        
        #Create an Objects List
        self.objects = []

        #Set the Game State
        self.game_state = GAME_STATES.OVERWORLD.value
        self.sub_state = GAME_STATES.NULL_STATE.value

        #Set the Text Speed
        self.text_speed	= TEXT_MEDIUM

        #Set REQSS Variables
        self.event_queue = [] #A list of base level simultaneous events
        self.event_stack = [] #A list of currently ongoing events arranged in layers
        self.stack_index = 0  #Denotes where the currently running event is in the stack
        
        #Define Important Pointers
        self.current_room = -1
        self.main_player = -1
        self.player_weapon = -1
        
        #Create Textbox
        self.textbox = core.instance_create(self, 0, 0, textbox_objects.obj_textbox())
        self.textbox.visible = False

        #Define Skill Info
        self.selected_class = "Warrior"
        self.selected_skills = []

        #Read in High Score
        score_file = open("score.dat", "r")
        self.high_score = int(score_file.readline())
        score_file.close()

        self.previous_song = SNG_NULL		   #The Song that Last Played
        self.current_song  = SNG_NULL		   #The Song that Is Currently Playing
        self.currently_playing = SNG_NULL[MUSIC_INTRO_SEGMENT]
		
		#Play the Null Song to Start
        music_core.audio_play_sound(self, SNG_NULL[MUSIC_INTRO_SEGMENT], False)

        #Create the Title Screen
        core.instance_create(self, 0, 0, title_menu.obj_Title_Menu())
        
    #Run Every Frame
    def update(self):
        #Check if An Exit Needs to Be Created
        if (self.current_room != -1 and self.current_room.num_enemies == 0 and not self.current_room.exit_exists):
            music_core.audio_play_sfx(self, "sfx_stairs_appear", False)
            self.current_room.create_exit()

        #Update Music
        music_core.scr_music_system(self, self.previous_song, self.current_song)
            
        #Update Events
        
        #Reset the Stack Index
        self.stack_index = 0
        
        #Is there An Event In the Queue?
        if len(self.event_queue) > 0:
        
            #Is there A Sub Event to Run?
            if len(self.event_stack) > 0:
            
                #Run the Sub Event
                self.event_stack[self.stack_index] = ec.scr_run_event(self, self.event_stack[self.stack_index])
                
                #Is the Sub Event Over?
                if self.event_stack[0][EVENT_DONE]:
                
                    #Remove the Sub Event
                    self.event_stack.pop(0)
                    
                    #Are there More Sub Events?
                    if len(self.event_stack) > 0:
                    
                        #Progress the Previous Sub Event
                        self.event_stack[0][EVENT_CONTINUE_SCRIPT] += 1
                    
                    else:
                        #Progress the Main Event
                        self.event_queue[0][EVENT_CONTINUE_SCRIPT] += 1
                    
                
            
            else:
                #Run the Main Event
                self.event_queue[0] = ec.scr_run_event(self, self.event_queue[0])

                #Is the Main Event Over?
                if self.event_queue[0][EVENT_DONE]:
                
                    #Remove the Event From the Queue
                    self.event_queue.pop(0)    

        if not pygame.mixer.music.get_busy():
            self.currently_playing = SNG_NULL[MUSIC_INTRO_SEGMENT]

    def create_run(self):
        #Create a Test Room
        self.test_room = dr.DungeonRoom(self, 40, 20, 1)
        
        #Create the Player
        self.main_player = core.instance_create(self, 32, 32, player.Player("Lucas", self.selected_class, self.selected_skills))

        #Show the Textbox
        self.textbox.visible = True

        #Assign the Current Room
        self.current_room = self.test_room

        #Place the Player in the Room
        self.main_player.goto_start_tile(self)


#The Main Function
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

    #Setup the Controllers
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joystick in joysticks:
        print(joystick.get_name())

    
    #Create the Manager
    main = MainManager()
    
    #Main Loop
    while running:
        #Update Frame Rate
        time_delta = clock.tick(FRAME_RATE)/1000.0

        #Check for a Main Quit
        if (main.quit):
            running = False


        #Event Handling
        for event in pygame.event.get():
            
            #Event: QUIT
            if event.type == pygame.QUIT:
                #Set Running to False
                running = False
            
            #Event: INPUT
            if (len(joysticks) > 0):
                if event.type==pygame.JOYBUTTONDOWN:
                    if event.button == 13:
                        if main.im.left != 1:
                            main.im.left_pressed = 1
                        
                        main.im.left = 1
                    else:
                        main.im.left = 0
                        main.im.left_pressed = 0

                    if event.button == 14:
                        if main.im.right != 1:
                            main.im.right_pressed = 1
                        
                        main.im.right = 1
                    else:
                        main.im.right = 0
                        main.im.right_pressed = 0

                    if event.button == 11:
                        if main.im.up != 1:
                            main.im.up_pressed = 1
                        
                        main.im.up = 1
                    else:
                        main.im.up = 0
                        main.im.up_pressed = 0

                    if event.button == 12:
                        if main.im.down != 1:
                            main.im.down_pressed = 1
                        
                        main.im.down = 1
                    else:
                        main.im.down = 0
                        main.im.down_pressed = 0
                    #A
                    if event.button==0:
                        if main.im.a != 1:
                            main.im.a_pressed = 1
                        
                        main.im.a = 1
                    else:
                        main.im.a = 0
                        main.im.a_pressed = 0
                    #B
                    if event.button==1:
                        if main.im.b != 1:
                            main.im.b_pressed = 1
                        
                        main.im.b = 1
                    else:
                        main.im.b = 0
                        main.im.b_pressed = 0

                    #X
                    if event.button==2:
                        if main.im.x != 1:
                            main.im.x_pressed = 1
                        
                        main.im.x = 1
                    else:
                        main.im.x = 0
                        main.im.x_pressed = 0

                    #Y
                    if event.button==3:
                        if main.im.y != 1:
                            main.im.y_pressed = 1
                        
                        main.im.y = 1
                    else:
                        main.im.y = 0
                        main.im.y_pressed = 0

                    #Z
                    if event.button==9:
                        if main.im.z != 1:
                            main.im.z_pressed = 1
                        
                        main.im.z = 1
                    else:
                        main.im.z = 0
                        main.im.z_pressed = 0
                        
                if event.type==pygame.JOYBUTTONUP:
                    if event.button == 13:
                        main.im.left_pressed = 0
                        main.im.left = 0
                        
                    if event.button == 14:
                        main.im.right_pressed = 0
                        main.im.right = 0
                        
                    if event.button == 11:
                        main.im.up_pressed = 0
                        main.im.up = 0
                        
                    if event.button == 12:
                        main.im.down_pressed = 0
                        main.im.down = 0
            else:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        if main.im.left != 1:
                            main.im.left_pressed = 1
                        
                        main.im.left = 1
                    else:
                        main.im.left = 0
                        main.im.left_pressed = 0

                    if event.key==pygame.K_RIGHT:
                        if main.im.right != 1:
                            main.im.right_pressed = 1
                        
                        main.im.right = 1
                    else:
                        main.im.right = 0
                        main.im.right_pressed = 0

                    if event.key==pygame.K_UP:
                        if main.im.up != 1:
                            main.im.up_pressed = 1
                        
                        main.im.up = 1
                    else:
                        main.im.up = 0
                        main.im.up_pressed = 0

                    if event.key==pygame.K_DOWN:
                        if main.im.down != 1:
                            main.im.down_pressed = 1
                        
                        main.im.down = 1
                    else:
                        main.im.down = 0
                        main.im.down_pressed = 0
                    
                    if event.key==pygame.K_z:
                        if main.im.a != 1:
                            main.im.a_pressed = 1
                        
                        main.im.a = 1
                    else:
                        main.im.a = 0
                        main.im.a_pressed = 0

                    if event.key==pygame.K_x:
                        if main.im.b != 1:
                            main.im.b_pressed = 1
                        
                        main.im.b = 1
                    else:
                        main.im.b = 0
                        main.im.b_pressed = 0
                        
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT:
                        main.im.left_pressed = 0
                        main.im.left = 0
                        
                    if event.key==pygame.K_RIGHT:
                        main.im.right_pressed = 0
                        main.im.right = 0
                        
                    if event.key==pygame.K_UP:
                        main.im.up_pressed = 0
                        main.im.up = 0
                        
                    if event.key==pygame.K_DOWN:
                        main.im.down_pressed = 0
                        main.im.down = 0

                

        #Run Update Logic
        main.update()

        for i in range(len(main.objects)):
            if (i < len(main.objects)):
                main.objects[i].update(main)
        
        #Clear the Old Screen
        screen.fill(pygame.Color('#ffefff'))

        #Draw Graphics
        if (main.current_room != -1):
            display_room(screen, main.current_room, main.basic_tiles, core.TILE_SIZE)
        
        draw_sprites(screen, main.objects, main.sprites)
        
        #Update the Display
        pygame.display.update()
      
        
#Run main
engine_main()
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:29:06 2022

@author: lucas
"""

from constants import CENTER_LEFT, GAME_STATES
import core
from font_scripts import scr_place_object_text
import weapons
import dungeon_room as dr
from weapons import obj_Weapon

class Player(core.Object):
    def __init__(self, name):
        core.Object.__init__(self, "spr_player_right", 1, True)
        
        self.name = name

    def create(self, main):
        self.hsp = 0
        self.vsp = 0

        self.health = 100
        self.max_health = 100

        self.damage = 10

        self.iframes = 0
        
        self.walkSpeed = 4

        self.attacking = False

        self.gold = 0

        self.direction = [1, 0]

        self.hud = core.instance_create(main, 0, 0, Player_HUD(self))
        
    def update(self, main):
        core.Object.update(self, main)
        
        moveLeft = -1 * int(main.im.left)
        moveRight = int(main.im.right)
        moveUp = -1 * int(main.im.up)
        moveDown = int(main.im.down)
        
        if (not self.attacking and main.sub_state != GAME_STATES.DIALOGUE.value):
            self.hsp = self.walkSpeed * (moveLeft + moveRight)
            self.vsp = self.walkSpeed * (moveUp + moveDown)
        else:
            self.hsp = 0
            self.vsp = 0
        
        
        #Horizontal Collisions
        if (self.hsp > 0):
            collision_found = False
            i = 0

            while (i <= 32 and not collision_found):

                if (core.tile_at_coord(main.current_room.movement, self.x + 32 + self.hsp, self.y + i) == 1):
                    while (core.tile_at_coord(main.current_room.movement, self.x + 32 + 1, self.y + i) == 0):
                        self.x += 1

                    collision_found = True

                    self.hsp = 0

                i += 1
                
        elif (self.hsp < 0):
            collision_found = False
            i = 0

            while (i <= 32 and not collision_found):

                if (core.tile_at_coord(main.current_room.movement, self.x + self.hsp, self.y + i) == 1):
                    while (core.tile_at_coord(main.current_room.movement, self.x - 1, self.y + i) == 0):
                        self.x -= 1
                    
                    collision_found = True

                    self.hsp = 0

                i += 1
        
        self.x += self.hsp
        
        
        #Vertical Collisions
        if (self.vsp > 0):
            collision_found = False
            i = 0

            while (i <= 32 and not collision_found):

                if (core.tile_at_coord(main.current_room.movement, self.x + i, self.y + 32 + self.vsp) == 1):
                    while (core.tile_at_coord(main.current_room.movement, self.x + i, self.y + 32 + 1) == 0):
                        self.y += 1
                        
                    collision_found = True

                    self.vsp = 0

                i += 1

        elif (self.vsp < 0):
            collision_found = False
            i = 0

            while (i <= 32 and not collision_found):

                if (core.tile_at_coord(main.current_room.movement, self.x + i, self.y + self.vsp) == 1):
                    while (core.tile_at_coord(main.current_room.movement, self.x + i, self.y - 1) == 0):
                        self.y -= 1
                    
                    collision_found = True

                    self.vsp = 0
                
                i += 1
        
        self.y += self.vsp

        #Collision With Stairs
        if (core.tile_at_coord(main.current_room.tiles, self.x + 16, self.y + 16) == 2):
            main.current_room = dr.DungeonRoom(main, 40, 20, main.current_room.difficulty + 1)

            self.goto_start_tile(main)

        #Attacking
        if (self.hsp == 0 and self.vsp == 0 and not self.attacking and main.im.b_pressed and main.sub_state != GAME_STATES.DIALOGUE.value):
            
            main.im.b_pressed = False
            self.attacking = True

            weapon = -1

            if (self.direction[0] == 1):
                weapon = core.instance_create(main, self.x + 24, self.y, obj_Weapon())
                weapon.image_index = 0
            elif (self.direction[0] == -1):
                weapon = core.instance_create(main, self.x - 24, self.y, obj_Weapon())
                weapon.image_index = 1
            elif (self.direction[1] == 1):
                weapon = core.instance_create(main, self.x, self.y + 24, obj_Weapon())
                weapon.image_index = 2
            elif (self.direction[1] == -1):
                weapon = core.instance_create(main, self.x, self.y - 24, obj_Weapon())
                weapon.image_index = 3

            weapon.owner = self
            main.player_weapon = weapon

        #Set a Direction and Update Animations
        if (self.hsp > 0):
            self.direction = [1, 0]
            self.sprite_index = "spr_player_right"
        elif (self.hsp < 0):
            self.direction = [-1, 0]
            self.sprite_index = "spr_player_left"

        if (self.vsp > 0):
            self.direction = [0, 1]
            self.sprite_index = "spr_player_down"
        elif (self.vsp < 0):
            self.direction = [0, -1]
            self.sprite_index = "spr_player_up"

        #Update Invincibility Frames
        if (self.iframes > 0):
            self.visible = (self.iframes % 2 == 0)

            self.iframes -= 1
        else:
            self.visible = True


            
    
    def goto_start_tile(self, main):
        for r in range(main.current_room.room_height):
                for c in range(main.current_room.room_width):
                    if (main.current_room.tiles[r][c] == 3):
                        self.x = c * core.TILE_SIZE
                        self.y = r * core.TILE_SIZE

                        #main.current_room.set_tile(c, r, 0, 0)
        

class Player_HUD(core.Object):
    def __init__(self, player):
        core.Object.__init__(self, "spr_player_hud", 1, True)

        self.player = player
        self.x = 8
        self.y = 8

        self.text = []

    def create(self, main):
        self.update_ui(main)

    def update_ui(self, main):
        for i in range(len(self.text)):
            core.instance_destroy(main, self.text[i])

        self.text = []
        self.text = scr_place_object_text(main, self, self.text, 2, 2, CENTER_LEFT, "Health: " + str(self.player.health) + " of " + str(self.player.max_health) + "   Gold: " + str(self.player.gold))
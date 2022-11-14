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
from weapons import obj_Bullet, obj_Weapon
from game_over_menu import obj_Game_Over_Menu

class Player(core.Object):
    def __init__(self, name, ch_class, skills):
        core.Object.__init__(self, "spr_player_right", 1, True)
        
        self.name = name
        self.character_class = ch_class
        self.skills = skills

    def create(self, main):
        self.hsp = 0
        self.vsp = 0

        self.alive = False

        self.health = 100
        self.max_health = 100

        self.damage = 10

        self.iframes = 0
        
        self.walkSpeed = 4

        self.attacking = False

        self.gold = 0

        self.direction = [1, 0]

        self.hud = core.instance_create(main, 0, 0, Player_HUD(self))

        self.slam_active = False
        self.bashing = False
        self.blood_striking = False
        self.shield_blocking = False
        self.counter_attacking = False
        
    def update(self, main):
        core.Object.update(self, main)
        
        if (self.health <= 0):
            self.health = 0
            self.alive = False
            main.main_player = -1
            core.instance_create(main, 0, 0, obj_Game_Over_Menu())
            main.current_room = -1
            core.instance_destroy(main, self)


        moveLeft = -1 * int(main.im.left)
        moveRight = int(main.im.right)
        moveUp = -1 * int(main.im.up)
        moveDown = int(main.im.down)
        
        if (not self.attacking and main.sub_state != GAME_STATES.DIALOGUE.value):
            if ((self.have_skill("beserking") and self.health < self.max_health * 0.5)
                or (self.have_skill("rage") and self.get_skill("rage").activation > 0)):
                self.hsp = (self.walkSpeed * 2) * (moveLeft + moveRight)
                self.vsp = (self.walkSpeed * 2) * (moveUp + moveDown)
            else:
                self.hsp = self.walkSpeed * (moveLeft + moveRight)
                self.vsp = self.walkSpeed * (moveUp + moveDown)
        else:
            self.hsp = 0
            self.vsp = 0
        
        
        #Horizontal Collisions
        if (self.hsp > 0):
            collision_found = False
            i = 1

            while (i < 32 and not collision_found):

                if (core.tile_at_coord(main.current_room.movement, self.x + 32 + self.hsp, self.y + i) == 1):
                    while (core.tile_at_coord(main.current_room.movement, self.x + 32 + 1, self.y + i) == 0):
                        self.x += 1

                    collision_found = True

                    self.hsp = 0

                i += 1
                
        elif (self.hsp < 0):
            collision_found = False
            i = 1

            while (i < 32 and not collision_found):

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
            i = 1

            while (i < 32 and not collision_found):

                if (core.tile_at_coord(main.current_room.movement, self.x + i, self.y + 32 + self.vsp) == 1):
                    while (core.tile_at_coord(main.current_room.movement, self.x + i, self.y + 32 + 1) == 0):
                        self.y += 1
                        
                    collision_found = True

                    self.vsp = 0

                i += 1

        elif (self.vsp < 0):
            collision_found = False
            i = 1

            while (i < 32 and not collision_found):

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

            if (self.character_class == "warrior"):
                if (self.have_skill("whirlwind") and self.get_skill("whirlwind").cooldown == 0):
                    self.get_skill("whirlwind").cooldown = self.get_skill("whirlwind").max_cooldown
                    weapon = self.attack(main, "spr_whirlwind")
                elif (self.have_skill("shield_bash") and self.get_skill("shield_bash").cooldown == 0):
                    self.get_skill("shield_bash").cooldown = self.get_skill("shield_bash").max_cooldown
                    weapon = self.attack(main, "spr_shield_bash")
                elif (self.have_skill("slam") and self.get_skill("slam").cooldown == 0 and not self.slam_active):
                    self.slam_active = True
                elif (self.have_skill("rage") and self.get_skill("rage").cooldown == 0):
                    self.get_skill("rage").cooldown = self.get_skill("rage").max_cooldown
                    self.get_skill("rage").activation = self.get_skill("rage").max_activation
                elif (self.have_skill("shield_block") and self.get_skill("shield_block").cooldown == 0):
                    self.get_skill("shield_block").cooldown = self.get_skill("shield_block").max_cooldown
                    self.get_skill("shield_block").activation = self.get_skill("shield_block").max_activation
                    self.shield_blocking = True
                elif (self.have_skill("counter_attack") and self.get_skill("counter_attack").cooldown == 0):
                    self.get_skill("counter_attack").cooldown = self.get_skill("counter_attack").max_cooldown
                    self.get_skill("counter_attack").activation = self.get_skill("counter_attack").max_activation
                    self.counter_attacking = True
                else:
                    if (self.have_skill("blood_strike") and self.get_skill("blood_strike").cooldown == 0):
                        self.get_skill("blood_strike").cooldown = self.get_skill("blood_strike").max_cooldown
                        self.blood_striking = True

                    weapon = self.attack(main, "spr_sword")
            elif (self.character_class == "ranger"):

                if (self.have_skill("multi_shot") and self.get_skill("multi_shot").cooldown == 0):
                    self.get_skill("multi_shot").cooldown = self.get_skill("multi_shot").max_cooldown
                    
                    #????????????
                else:
                    weapon = self.ranged_attack(main, "spr_ranged_attack", "spr_bullet")

            elif (self.character_class == "wizard"):

                
                weapon = self.attack(main, "spr_staff")

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

        #Update Skill Cooldowns
        self.reduce_cooldowns(1)
        self.reduce_activations(1)

        if (self.have_skill("shield_block") and self.get_skill("shield_block").activation == 0):
            self.shield_blocking = False

        if (self.have_skill("counter_attack") and self.get_skill("counter_attack").activation == 0):
            self.counter_attacking = False


            
    
    def goto_start_tile(self, main):
        for r in range(main.current_room.room_height):
                for c in range(main.current_room.room_width):
                    if (main.current_room.tiles[r][c] == 3):
                        self.x = c * core.TILE_SIZE
                        self.y = r * core.TILE_SIZE
    

    def have_skill(self, s):
        for i in range(len(self.skills)):
            if (self.skills[i].name == s):
                return True
        
        return False

    def get_skill(self, s):
        for i in range(len(self.skills)):
            if (self.skills[i].name == s):
                return self.skills[i]
        
        return -1

    def reduce_cooldowns(self, a):
        for i in range(len(self.skills)):
            self.skills[i].cooldown = max(0, self.skills[i].cooldown - a)

    def reduce_activations(self, a):
        for i in range(len(self.skills)):
            self.skills[i].activation = max(0, self.skills[i].activation - a)
    def restore_health(self, a):
        self.health = min(self.health + a, self.max_health)

    def attack(self, main, weapon_sprite):
        weapon = -1

        if (self.direction[0] == 1):
            weapon = core.instance_create(main, self.x + 24, self.y, obj_Weapon())
            weapon.sprite_index = weapon_sprite
            weapon.image_index = 0
        elif (self.direction[0] == -1):
            weapon = core.instance_create(main, self.x - 24, self.y, obj_Weapon())
            weapon.sprite_index = weapon_sprite
            weapon.image_index = 1
        elif (self.direction[1] == 1):
            weapon = core.instance_create(main, self.x, self.y + 24, obj_Weapon())
            weapon.sprite_index = weapon_sprite
            weapon.image_index = 2
        elif (self.direction[1] == -1):
            weapon = core.instance_create(main, self.x, self.y - 24, obj_Weapon())
            weapon.sprite_index = weapon_sprite
            weapon.image_index = 3

        return weapon

    def ranged_attack(self, main, attack_sprite, bullet_sprite):
        weapon = -1

        self.sprite_index = attack_sprite

        if (self.direction[0] == 1):
            weapon = core.instance_create(main, self.x + 24, self.y, obj_Bullet())
            self.image_index = 0
        elif (self.direction[0] == -1):
            weapon = core.instance_create(main, self.x - 24, self.y, obj_Bullet())
            self.image_index = 1
        elif (self.direction[1] == 1):
            weapon = core.instance_create(main, self.x, self.y + 24, obj_Bullet())
            self.image_index = 2
        elif (self.direction[1] == -1):
            weapon = core.instance_create(main, self.x, self.y - 24, obj_Bullet())
            self.image_index = 3

        weapon.sprite_index = bullet_sprite
        weapon.direction = [self.direction[0], self.direction[1]]

        return weapon

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
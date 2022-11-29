import core
import music_core
import constants
import gold
import random

class obj_Enemy(core.Object):
    def __init__(self, main, sprite, frames):
        core.Object.__init__(self, main, sprite, frames, True)  

    def create(self, main):
        self.speed = 0
        self.speed = 0

        self.walkspeed = 0

        self.hp = 0
        self.iframes = 0

        self.damage = 0

        self.stunned = False

        self.drop_chance = 0.2
        self.drop_amount = random.randint(1, 3)

    def update(self, main):
        if (main.main_player == -1):
            core.instance_destroy(main, self)
        else:
            #Update Invincibility Frames
            if (self.iframes > 0):
                self.visible = (self.iframes % 2 == 0)

                self.iframes -= 1
            else:
                self.visible = True

            #Check For Death
            if (self.hp <= 0):
                if (main.main_player.have_skill("headhunter")):
                    main.main_player.damage += 0.1

                if (main.main_player.have_skill("victory_rush")):
                    main.main_player.restore_health(10)

                core.instance_destroy(main, self)

            #Take Damage
            if (main.player_weapon != -1 and self.iframes == 0 and core.scr_collision(self, main.player_weapon)):

                if (main.main_player.have_skill("relentless")):
                    main.main_player.reduce_cooldown(0.5)

                damage_amount = main.main_player.damage

                if (main.main_player.have_skill("heroic_strike") and main.main_player.get_skill("heroic_strike").cooldown == 0):
                    damage_amount *= 1.5
                    main.main_player.get_skill("heroic_strike").cooldown = main.main_player.get_skill("heroic_strike").max_cooldown
                
                if (main.main_player.have_skill("rage") and self.get_skill("rage").activation > 0):
                    damage_amount *= 2
                
                if (main.main_player.have_skill("beserking") and main.main_player.health < main.main_player.max_health * 0.5):
                    damage_amount += 5

                if (main.main_player.have_skill("ravage") and self.get_skill("ravage").activation > 0):
                    damage_amount += 10

                if (main.main_player.slam_active):
                    damage_amount += damage_amount * 2
                    main.main_player.slam_active = False
                    main.main_player.get_skill("slam").cooldown = main.main_player.get_skill("slam").max_cooldown

                if (main.main_player.blood_striking):
                    main.main_player.blood_striking = False
                    blood_damage = main.main_player.health * 0.25

                    main.main_player.health -= blood_damage
                    damage_amount += blood_damage

                if (main.main_player.bashing):
                    main.main_player.bashing = False
                    self.stunned = True

                self.hp -= damage_amount

                self.iframes = 1 * constants.FRAME_RATE

                music_core.audio_play_sfx(main, "sfx_damage", False)

            #Deal Contact Damage
            if (main.main_player.iframes == 0 and core.scr_collision(self, main.main_player)):
                
                if(main.main_player.shield_blocking):
                    main.main_player.shield_blocking = False
                else:
                    damage_amount = self.damage

                    if (main.main_player.counter_attacking):
                        main.main_player.counter_attacking = False
                        
                        self.hp -= self.damage * 1.25
                        self.iframes = 1 * constants.FRAME_RATE
                        
                        damage_amount *= 0.5
                    elif (main.main_player.charging):
                        main.main_player.charging = False
                        main.main_player.attacking = False
                        main.main_player.get_skill("charge").cooldown = main.main_player.get_skill("charge").max_cooldown

                        self.hp -= main.main_player.damage
                        self.iframes = 1 * constants.FRAME_RATE
                        main.main_player.iframes = 1 * constants.FRAME_RATE

                    main.main_player.health = max(0, main.main_player.health - damage_amount)

                    main.main_player.iframes = 1 * constants.FRAME_RATE

                    main.main_player.hud.update_ui(main)

                    music_core.audio_play_sfx(main, "sfx_damage", False)

    
    def destroy(self, main):
        if (main.main_player != -1):
            threshold = random.randint(1, 100)

            if (self.drop_chance <= (threshold/100.0)):
                core.instance_create(main, self.x, self.y, gold.obj_Gold(main, self.drop_amount))

            main.current_room.num_enemies -= 1


class obj_Blob(obj_Enemy):
    def __init__(self, main):
        obj_Enemy.__init__(self, main, "spr_blob", 18)

    def create(self, main):
        obj_Enemy.create(self, main)

        self.hp = 10
        self.damage = 5

        direc = random.randint(0, 1)

        if (direc == 0):
            self.image_xscale = 1
        else:
            self.image_xscale = -1


class obj_Bat(obj_Enemy):
    def __init__(self, main):
        obj_Enemy.__init__(self, main, "spr_bat", 12)

    def create(self, main):
        obj_Enemy.create(self, main)

        self.hp = 10
        self.damage = 5

        self.timer = 0
        self.max_timer = 180

        self.h_move = 0
        self.v_move = 0

    def update(self, main):
        obj_Enemy.update(self, main)

        if (main.current_room != -1):
            if (self.timer > 0):
                self.timer -= 1
            else:
                self.timer = self.max_timer
                self.h_move = random.randint(-2, 2)
                self.v_move = random.randint(-2, 2)

            self.x = max(32, min(self.x + self.h_move, main.current_room.room_width * constants.TILE_SIZE - 32))
            self.y = max(32, min(self.y + self.v_move, main.current_room.room_height * constants.TILE_SIZE - 32))

        if (self.h_move > 0):
            self.image_xscale = 1
        elif (self.h_move < 0):
            self.image_xscale = -1
            


class obj_Spike(obj_Enemy):
    def __init__(self, main):
        obj_Enemy.__init__(self, main, "spr_spike", 18)

    def create(self, main):
        obj_Enemy.create(self, main)

        self.hp = 25
        self.damage = 10

        self.directions = ['h', 'v']
        self.direction = self.directions[random.randint(0, 1)]
        
        self.speed = 0
        self.move_speed = 8

        self.timer = 0
        self.max_timer = 240

    def update(self, main):
        obj_Enemy.update(self, main)

        if (self.timer > 0):
            self.timer -= 1
        elif (self.speed == 0):
            self.timer = self.max_timer
            self.speed = self.move_speed

        if (self.direction == 'h'):
            #Horizontal Collisions
                if (self.speed > 0):
                    collision_found = False
                    i = 1

                    while (i < 32 and not collision_found):

                        if (core.tile_at_coord(main.current_room.movement, self.x + 32 + self.speed, self.y + i) == 1):
                            while (core.tile_at_coord(main.current_room.movement, self.x + 32 + 1, self.y + i) == 0):
                                self.x += 1

                            collision_found = True
                            self.speed = 0
                            self.move_speed *= -1

                            
                        i += 1
                        
                elif (self.speed < 0):
                    collision_found = False
                    i = 1

                    while (i < 32 and not collision_found):

                        if (core.tile_at_coord(main.current_room.movement, self.x + self.speed, self.y + i) == 1):
                            while (core.tile_at_coord(main.current_room.movement, self.x - 1, self.y + i) == 0):
                                self.x -= 1
                            
                            collision_found = True
                            self.speed = 0
                            self.move_speed *= -1

                        i += 1
                
                self.x += self.speed

                if (self.speed > 0):
                    self.image_xscale = 1
                elif (self.speed < 0):
                    self.image_xscale = -1
            
        else:
            #Vertical Collisions
            if (self.speed > 0):
                collision_found = False
                i = 1

                while (i < 32 and not collision_found):

                    if (core.tile_at_coord(main.current_room.movement, self.x + i, self.y + 32 + self.speed) == 1):
                        while (core.tile_at_coord(main.current_room.movement, self.x + i, self.y + 32 + 1) == 0):
                            self.y += 1
                            
                        collision_found = True
                        self.speed = 0
                        self.move_speed *= -1

                    i += 1

            elif (self.speed < 0):
                collision_found = False
                i = 1

                while (i < 32 and not collision_found):

                    if (core.tile_at_coord(main.current_room.movement, self.x + i, self.y + self.speed) == 1):
                        while (core.tile_at_coord(main.current_room.movement, self.x + i, self.y - 1) == 0):
                            self.y -= 1
                        
                        collision_found = True
                        self.speed = 0
                        self.move_speed *= -1
                    
                    i += 1
            
            self.y += self.speed

            if (self.speed > 0):
                self.image_yscale = 1
            elif (self.speed < 0):
                self.image_yscale = -1
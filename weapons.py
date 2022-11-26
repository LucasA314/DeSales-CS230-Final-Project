from re import S
import core
import music_core

class obj_Weapon(core.Object):
    def __init__(self):
        core.Object.__init__(self, "spr_sword", 1, True)

    def create(self, main):
        self.image_speed = 0

        self.remaining_frames = 60

        self.owner = -1

        music_core.audio_play_sfx(main, "sfx_attack", False)

    def update(self, main):
        if (main.main_player == -1):
            core.instance_destroy(main, self)

        self.remaining_frames -= 1

        if (self.remaining_frames == 0):
            core.instance_destroy(main, self)

    def destroy(self, main):
        main.player_weapon = -1

        if (self.owner != -1):
            self.owner.attacking = False

class obj_Bullet(core.Object):
    def __init__(self):
        core.Object.__init__(self, "spr_bullet", 1, True)
    
    def create(self, main):
        self.direction = [0, 0]

        self.hsp = 0
        self.vsp = 0
        
        self.speed = 4

    def update(self, main):
        if (main.main_player == -1):
            core.instance_destroy(main, self)

        self.hsp = self.direction[0] * self.speed
        self.vsp = self.direction[1] * self.speed

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
                    core.instance_destroy(self)

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
                    core.instance_destroy(self)

                i += 1
        
        
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
                    core.instance_destroy(self)

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
                    core.instance_destroy(self)
                
                i += 1

        self.x += self.hsp
        self.y += self.vsp
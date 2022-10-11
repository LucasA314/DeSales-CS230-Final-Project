
import core
import gold
import random

class obj_Enemy(core.Object):
    def __init__(self, sprite, frames):
        core.Object.__init__(self, sprite, frames, True)

        

    def create(self, main):
        self.vsp = 0
        self.hsp = 0

        self.walkspeed = 0

        self.hp = 0
        self.iframes = 0

        self.damage = 0

        self.drop_chance = 0.2
        self.drop_amount = random.randint(1, 3)

    def update(self, main):
        #Update Invincibility Frames
        if (self.iframes > 0):
            self.visible = (self.iframes % 2 == 0)

            self.iframes -= 1
        else:
            self.visible = True

        #Check For Death
        if (self.hp <= 0):
            core.instance_destroy(main, self)

        #Take Damage
        if (main.player_weapon != -1 and self.iframes == 0 and core.scr_collision(self, main.player_weapon)):
            self.hp -= main.main_player.damage

            self.iframes = 60

        #Deal Contact Damage
        if (main.main_player.iframes == 0 and core.scr_collision(self, main.main_player)):
            main.main_player.health = max(0, main.main_player.health - self.damage)

            main.main_player.iframes = 60

            main.main_player.hud.update_ui(main)

    
    def destroy(self, main):
        threshold = random.randint(1, 100)

        if (self.drop_chance <= (threshold/100.0)):
            core.instance_create(main, self.x, self.y, gold.obj_Gold(self.drop_amount))

        main.current_room.num_enemies -= 1


class obj_Blob(obj_Enemy):
    def __init__(self):
        obj_Enemy.__init__(self, "spr_blob", 1)

    def create(self, main):
        obj_Enemy.create(self, main)

        self.hp = 10
        self.damage = 5

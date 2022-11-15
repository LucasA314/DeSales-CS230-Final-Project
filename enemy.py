
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

                self.iframes = 60

            #Deal Contact Damage
            if (main.main_player.iframes == 0 and core.scr_collision(self, main.main_player)):
                
                if(main.main_player.shield_blocking):
                    main.main_player.shield_blocking = False
                else:
                    damage_amount = self.damage

                    if (main.main_player.counter_attacking):
                        main.main_player.counter_attacking = False
                        
                        self.hp -= self.damage * 1.25
                        self.iframes = 60
                        
                        damage_amount *= 0.5


                    main.main_player.health = max(0, main.main_player.health - damage_amount)

                    main.main_player.iframes = 60

                    main.main_player.hud.update_ui(main)

    
    def destroy(self, main):
        if (main.main_player != -1):
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

import core

class obj_Weapon(core.Object):
    def __init__(self):
        core.Object.__init__(self, "spr_sword", 1, True)

    def create(self, main):
        self.image_speed = 0

        self.remaining_frames = 60

        self.owner = -1

    def update(self, main):
        self.remaining_frames -= 1

        if (self.remaining_frames == 0):
            core.instance_destroy(main, self)

    def destroy(self, main):
        main.player_weapon = -1

        if (self.owner != -1):
            self.owner.attacking = False
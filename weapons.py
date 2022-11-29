import constants
import core
import music_core

class obj_Weapon(core.Object):
    def __init__(self, main):
        core.Object.__init__(self, main, "spr_sword", 1, True)

    def create(self, main):
        self.image_speed = 0

        self.remaining_frames = 1 * constants.FRAME_RATE

        self.owner = -1

        music_core.audio_play_sfx(main, "sfx_attack", False)

    def update(self, main):
        if (main.main_player == -1):
            core.instance_destroy(main, self)

        self.remaining_frames -= 1

        if (self.remaining_frames <= 0):
            core.instance_destroy(main, self)

    def destroy(self, main):
        main.player_weapon = -1

        if (self.owner != -1):
            self.owner.attacking = False
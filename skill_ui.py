import core
import constants
import font_scripts
from active_skill import Skill

class obj_Skill_UI(core.Object):
    def __init__(self):
        core.Object.__init__(self, "spr_textbox", 1, False)

        self.image_speed = 0
    
    def create(self, main):
        self.skill_1_array = []
        self.skill_2_array = []
        self.skill_3_array = []

    def update(self, main):
        if (main.main_player == -1):
            core.instance_destroy(main, self)
        else:
            #Set Position
            self.x = 0
            self.y = main.textbox.y

            self.skill_1_array  = font_scripts.scr_place_object_text(main, self, self.skill_1_array,  256, 2, constants.CENTER_LEFT, "Skill 1: " + str(main.selected_skills[0].name) + "     Cooldown: " + str(main.selected_skills[0].cooldown))
            self.skill_2_array  = font_scripts.scr_place_object_text(main, self, self.skill_2_array,  256, 16, constants.CENTER_LEFT, "Skill 2: " + str(main.selected_skills[1].name) + "     Cooldown: " + str(main.selected_skills[1].cooldown))
            self.skill_3_array  = font_scripts.scr_place_object_text(main, self, self.skill_3_array,  256, 30, constants.CENTER_LEFT, "Skill 3: " + str(main.selected_skills[2].name) + "     Cooldown: " + str(main.selected_skills[2].cooldown))

    def destroy(self, main):
        font_scripts.scr_reset_letters(self.skill_1_array)
        font_scripts.scr_reset_letters(self.skill_2_array)
        font_scripts.scr_reset_letters(self.skill_3_array)
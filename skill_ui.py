import core
import constants
import font_scripts
from skill import Skill

class obj_Skill_UI(core.Object):
    def __init__(self, main):
        core.Object.__init__(self, main, "spr_textbox", 1, False)

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

            skill_txt = "Skill {num}: {skill}     Cooldown: {cool}"
            skill_txt_p = "Skill {num}: {skill}"

            self.skill_1_array = font_scripts.scr_reset_letters(self.skill_1_array)
            self.skill_2_array = font_scripts.scr_reset_letters(self.skill_2_array)
            self.skill_3_array = font_scripts.scr_reset_letters(self.skill_3_array)

            if (main.selected_skills[0].type == "Active"):
                self.skill_1_array  = font_scripts.scr_place_object_text(main, self, self.skill_1_array,  256, 2, constants.CENTER_LEFT, skill_txt.format(num = 1, skill = str(main.selected_skills[0].display_name), cool = str(main.selected_skills[0].cooldown)))
            else:
                self.skill_1_array  = font_scripts.scr_place_object_text(main, self, self.skill_1_array,  256, 2, constants.CENTER_LEFT, skill_txt_p.format(num = 1, skill = str(main.selected_skills[0].display_name)))
            
            if (main.selected_skills[1].type == "Active"):
                self.skill_2_array  = font_scripts.scr_place_object_text(main, self, self.skill_2_array,  256, 16, constants.CENTER_LEFT, skill_txt.format(num = 2, skill = str(main.selected_skills[1].display_name), cool = str(main.selected_skills[1].cooldown)))
            else:
                self.skill_2_array  = font_scripts.scr_place_object_text(main, self, self.skill_2_array,  256, 16, constants.CENTER_LEFT, skill_txt_p.format(num = 2, skill = str(main.selected_skills[1].display_name)))

            if (main.selected_skills[2].type == "Active"):
                self.skill_3_array  = font_scripts.scr_place_object_text(main, self, self.skill_3_array,  256, 30, constants.CENTER_LEFT, skill_txt.format(num = 3, skill = str(main.selected_skills[2].display_name), cool = str(main.selected_skills[2].cooldown)))
            else:
                self.skill_3_array  = font_scripts.scr_place_object_text(main, self, self.skill_3_array,  256, 30, constants.CENTER_LEFT, skill_txt_p.format(num = 3, skill = str(main.selected_skills[2].display_name)))   
            

    def destroy(self, main):
        font_scripts.scr_reset_letters(self.skill_1_array)
        font_scripts.scr_reset_letters(self.skill_2_array)
        font_scripts.scr_reset_letters(self.skill_3_array)
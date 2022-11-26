import core
import constants
import music_core
from active_skill import Skill

class obj_Skill_Select_Menu(core.Object):
    def __init__(self, main):
        core.Object.__init__(self, main, "spr_warrior_skill_1", 5, True)

        self.image_speed = 0
    
    def create(self, main):
        self.option = 0
        self.skill = 1

    def update(self, main):
        if (main.selected_class == "warrior"):
            if (self.skill == 1):
                self.sprite_index = "spr_warrior_skill_1"
            elif (self.skill == 2):
                self.sprite_index = "spr_warrior_skill_2"
            elif (self.skill == 3):
                self.sprite_index = "spr_warrior_skill_3"
        elif (main.selected_class == "ranger"):
            if (self.skill == 1):
                self.sprite_index = "spr_ranger_skill_1"
            elif (self.skill == 2):
                self.sprite_index = "spr_ranger_skill_2"
            elif (self.skill == 3):
                self.sprite_index = "spr_ranger_skill_3"
        elif (main.selected_class == "mage"):
            if (self.skill == 1):
                self.sprite_index = "spr_mage_skill_1"
            elif (self.skill == 2):
                self.sprite_index = "spr_mage_skill_2"
            elif (self.skill == 3):
                self.sprite_index = "spr_mage_skill_3"

        self.image_index = self.option

        if (main.im.up):
            main.im.up = False

            music_core.audio_play_sfx(main, "sfx_menu_move", False)

            if (self.option == 0):
                self.option = 4
            else:
                self.option -= 1

        if (main.im.down):
            main.im.down = False

            music_core.audio_play_sfx(main, "sfx_menu_move", False)

            if (self.option == 4):
                self.option = 0
            else:
                self.option += 1

        if (main.im.a):
            main.im.a = False

            music_core.audio_play_sfx(main, "sfx_menu_select", False)

            if (main.selected_class == "warrior"):
                if (self.skill == 1):
                    if (self.option == 0):
                        main.selected_skills.append(Skill(main, "whirlwind", "Whirlwind", "Active", 5 * 60, 0))
                    elif (self.option == 1):
                        main.selected_skills.append(Skill(main, "charge", "Charge", "Active", 10 * 60, 0))
                    elif (self.option == 2):
                        main.selected_skills.append(Skill(main, "headhunter", "Headhunter", "Passive", 0, 0))
                    elif (self.option == 3):
                        main.selected_skills.append(Skill(main, "rage", "Rage", "Active", 30 * 60, 10 * 60))
                    elif (self.option == 4):
                        main.selected_skills.append(Skill(main, "slam", "Slam", "Active", 7 * 60, 0))
                elif (self.skill == 2):
                    if (self.option == 0):
                        main.selected_skills.append(Skill(main, "shield_bash", "Shield Bash", "Active", 12 * 60, 0))
                    elif (self.option == 1):
                        main.selected_skills.append(Skill(main, "victory_rush", "Victory Rush", "Passive", 0, 0))
                    elif (self.option == 2):
                        main.selected_skills.append(Skill(main, "relentless", "Relentless", "Passive", 0, 0))
                    elif (self.option == 3):
                        main.selected_skills.append(Skill(main, "heroic_strike", "Heroic Strike", "Passive", 5 * 60, 0))
                    elif (self.option == 4):
                        main.selected_skills.append(Skill(main, "blood_strike", "Blood Strike", "Active", 1 * 60, 0))
                elif (self.skill == 3):
                    if (self.option == 0):
                        main.selected_skills.append(Skill(main, "berserking", "Berserking", "Passive", 0, 0))
                    elif (self.option == 1):
                        main.selected_skills.append(Skill(main, "recklessness", "Recklessness", "Passive", 0, 0))
                    elif (self.option == 2):
                        main.selected_skills.append(Skill(main, "shield_block", "Shield Block", "Active", 8 * 60, 2 * 60))
                    elif (self.option == 3):
                        main.selected_skills.append(Skill(main, "ravage", "Ravage", "Active", 6 * 60, 2 * 60))
                    elif (self.option == 4):
                        main.selected_skills.append(Skill(main, "counter_attack", "Counter Attack", "Active", 5 * 60, 5 * 60))



            if (self.skill < 3):
                self.skill += 1
            else:
                main.create_run()
                music_core.scr_set_song(main, constants.SNG_DUNGEON)
                core.instance_destroy(main, self)

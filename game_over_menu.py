import core
import music_core
from constants import EVENTS_LIST, GAME_STATES, SNG_GAME_OVER
from title_menu import obj_Title_Menu

import os

class obj_Game_Over_Menu(core.Object):
    def __init__(self, main, score):
        core.Object.__init__(self, main, "spr_game_over_menu", 1, True)

        self.menu = core.instance_create(main, self.x, self.y, obj_Game_Over_Menu_Image(main))
        
        self.score = score
    
    def create(self, main):
        music_core.scr_set_song(main, SNG_GAME_OVER)

        self.image_speed = 0

        messageToPrint = [[
                                "Final Score: " + str(self.score),
                                "High Score: " + str(main.high_score),
                            ]]

        #Add High Score Text
        if (main.high_score < self.score):
            messageToPrint = [[
                                        "Final Score: " + str(self.score) + "(NEW RECORD!)",
                                        "High Score: " + str(main.high_score),
                                    ]]
            main.high_score = self.score
            
            #Write the High Score
            cp = os.path.dirname(__file__)
            score_file = open(os.path.join(cp, "score.dat"), "w")
            score_file.write(str(main.high_score))
            score_file.close()

        core.scr_add_event_to_queue(main, EVENTS_LIST.printText.value, [messageToPrint])

    def update(self, main):

        if (main.im.a and main.sub_state != GAME_STATES.DIALOGUE.value):
            main.im.a = False

            core.instance_create(main, 0, 0, obj_Title_Menu(main))
            core.instance_destroy(main, self.menu)
            core.instance_destroy(main, self)

class obj_Game_Over_Menu_Image(core.Object):
    def __init__(self, main):
        core.Object.__init__(self, main, "spr_game_over_backdrop", 1, True)
        self.image_speed = 0
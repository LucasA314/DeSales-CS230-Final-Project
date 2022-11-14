import core
from title_menu import obj_Title_Menu

class obj_Game_Over_Menu(core.Object):
    def __init__(self):
        core.Object.__init__(self, "spr_game_over_menu", 1, True)
    
    def create(self, main):
        self.image_speed = 0

    def update(self, main):

        if (main.im.a):
            main.im.a = False

            core.instance_create(main, 0, 0, obj_Title_Menu())
            core.instance_destroy(main, self)

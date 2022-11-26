import core
import music_core
from class_select_menu import obj_Class_Select_Menu

class obj_Title_Menu(core.Object):
    def __init__(self, main):
        core.Object.__init__(self, main, "spr_title_menu", 2, True)

        self.image_speed = 0
    
    def create(self, main):
        self.option = 0

    def update(self, main):
        self.image_index = self.option

        if (main.im.up or main.im.down):
            main.im.up = False
            main.im.down = False

            music_core.audio_play_sfx(main, "sfx_menu_move", False)

            if (self.option == 0):
                self.option = 1
            else:
                self.option = 0

        if (main.im.a):
            main.im.a = False
            
            music_core.audio_play_sfx(main, "sfx_menu_select", False)

            if (self.option == 0):
        
                core.instance_create(main, 0, 0, obj_Class_Select_Menu(main))
                core.instance_destroy(main, self)
            else:
                main.quit = False

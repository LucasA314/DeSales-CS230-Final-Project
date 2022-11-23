import core
from skill_select_menu import obj_Skill_Select_Menu

class obj_Class_Select_Menu(core.Object):
    def __init__(self):
        core.Object.__init__(self, "spr_class_select_menu", 3, True)

        self.image_speed = 0
    
    def create(self, main):
        self.option = 0

        #SKIP THIS MENU
        main.selected_class = "warrior"

        core.instance_create(main, 0, 0, obj_Skill_Select_Menu())
        core.instance_destroy(main, self)

    def update(self, main):
        self.image_index = self.option

        if (main.im.up):
            main.im.up = False

            if (self.option == 0):
                self.option = 2
            else:
                self.option -= 1

        if (main.im.down):
            main.im.down = False

            if (self.option == 2):
                self.option = 0
            else:
                self.option += 1

        if (main.im.a):
            main.im.a = False

            if (self.option == 0):
                main.selected_class = "warrior"
            elif(self.option == 1):
                main.selected_class = "ranger"
            else:
                main.selected_class = "mage"
            
            core.instance_create(main, 0, 0, obj_Skill_Select_Menu())
            core.instance_destroy(main, self)

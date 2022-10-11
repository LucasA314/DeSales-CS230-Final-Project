import core

class obj_Title_Menu(core.Object):
    def __init__(self):
        core.Object.__init__(self, "spr_title_menu", 2, True)

        self.image_speed = 0
    
    def create(self, main):
        self.option = 0

    def update(self, main):
        self.image_index = self.option

        if (main.im.up or main.im.down):
            main.im.up = False
            main.im.down = False

            if (self.option == 0):
                self.option = 1
            else:
                self.option = 0

        if (main.im.a):
            main.im.a = False

            if (self.option == 0):
                main.create_run()

                core.instance_destroy(main, self)
